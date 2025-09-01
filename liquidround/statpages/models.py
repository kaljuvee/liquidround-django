from django.core.urlresolvers import reverse_lazy
from django.db import models
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
from django.utils.text import slugify
from redactor.fields import RedactorField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=128)
    text = RedactorField(upload_to='pages/', max_length=4294967295, blank=True, null=True)
    # text = models.TextField(max_length=4294967295, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    top_menu = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('statpages:page', args=[self.slug])

    def save(self):
        if self.slug == "":
            self.slug = slugify(self.title)
        return super(Page, self).save()


class Slider(models.Model):
    image = models.ImageField()
    position = models.PositiveIntegerField()
    titlle = models.CharField('Title', max_length=128)
    text = models.TextField('Description', max_length=1000, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return str(self.position)