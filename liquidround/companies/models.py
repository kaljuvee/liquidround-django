import PIL
import datetime
from PIL import Image

from django.db import models
from django.templatetags.static import static
from django.utils import timezone

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

# Create your models here.
class Industry(models.Model):
    title = models.CharField('Title', max_length=128)

    def __unicode__(self):
        return self.title

class Company(models.Model):
    title = models.CharField('Company name', max_length=128)
    slug = models.SlugField('Slug', blank=True, null=True)
    website = models.URLField('Website')
    industry = models.ForeignKey(Industry)
    role = models.CharField('Specific Role', max_length=256)
    country = models.CharField('Country', max_length=30, blank=True, null=True)
    city = models.CharField('City', max_length=30, blank=True, null=True)
    summary = models.TextField('Business Summary', max_length=40000, null=True, blank=True)
    team_desc = models.TextField('Team Description', max_length=40000, null=True, blank=True)
    pre_emption_rights = models.BooleanField('Pre-emption Rights', default=False)
    voting_rights = models.BooleanField('Voting Rights', default=False)
    class_a = models.BooleanField('Share Class A', default=False)
    class_b = models.BooleanField('Share Class B', default=False)

    F_STAGES = (
        ('seed', 'Seed'),
        ('series_a','Series A'),
        ('series_b','Series B'),
        ('series_c','Series C'),
        ('series_d','Series D'),
    )
    funding_stage = models.CharField('Current Funding State', max_length=30, choices=F_STAGES, default='', null=True, blank=True)
    published = models.BooleanField(default=False)

    def option_dict(self):
        result = {
            'data': unicode(self.id),
            'value': self.title,
        }
        return result

    def safe_dict(self):
        result = {
            'website': self.website,
            'industry': self.industry,
            'specificrole': self.role,
            'photos': [p.safe_dict() for p in self.photos.all()],
        }
        return result

    def brief_dict(self, user):
        result = {
            'id': self.pk,
            'slug': self.slug,
            'title': self.title,
            'equities_count': self.notification_set.filter(
                    user=user, 
                    listing__listing_type='equity',
                    listing__is_approved=True,
                    listing__is_closed=False,
                    listing__expireson__gt=datetime.datetime.now(),
                ).count(),
            'offers_count': self.notification_set.filter(
                    user=user, 
                    listing__listing_type='offer',
                    listing__is_approved=True,
                    listing__is_closed=False,
                    listing__expireson__gt=datetime.datetime.now(),
                ).count()
        }
        return result

    @property
    def logo(self):
        try:
            pics = self.photos.filter(is_main=True)[:1][0]
        except IndexError:
            return static('/static/images/assets/img/main/img12.jpg')
        return pics.optimized.url

    def __unicode__(self):
        return self.title


class Teammate(models.Model):
    company = models.ForeignKey(Company, related_name='team')
    title = models.CharField('Member, Occupation', max_length=128)


class Document(models.Model):
    company = models.ForeignKey(Company, related_name='documents')
    title = models.CharField('Document Title', max_length=255)
    doc = models.FileField('File', upload_to='attach')
    uploadedon = models.DateTimeField(default=timezone.now)
    uploadedby = models.ForeignKey('accounts.Profile', blank=True, null=True)


class Photo(models.Model):
    company = models.ForeignKey(Company, related_name='photos')
    image = models.ImageField('Image', upload_to='companies')
    is_main = models.BooleanField('Is main image?', default=False)
    optimized = ImageSpecField(source='image',
                               processors=[ResizeToFit(323,204, mat_color='#ffffff')],
                               format='JPEG',
                               options={'quality': 100}
                            )

    class Meta:
        ordering = ['-is_main']

    def safe_dict(self):
        result = {
            'id': self.id,
            'url': self.optimized.url,
            'is_main': 'checked' if self.is_main else '',
        }
        return result


@receiver(pre_save, sender=Company)
def save_alias(sender, instance, *args, **kwargs):
    if instance.slug == "":
        instance.slug = slugify(instance.title)