from django.db import models
from django.utils import timezone

# Create your models here.
from accounts.models import Profile
from companies.models import Company

class Listing(models.Model):
    user = models.ForeignKey(Profile,related_name='listings')
    company = models.ForeignKey(Company, related_name='listings')
    shares = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    LIST_TYPES = (
        ('equity','Equity'),
        ('offer', 'Offer'),
    )
    listing_type = models.CharField(max_length=15, choices=LIST_TYPES,
                                    default='equity')
    createdon = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    approvedon = models.DateTimeField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    closedon = models.DateTimeField(blank=True, null=True)
    expireson = models.DateTimeField(blank=True, null=True)
    prolong_code = models.CharField(max_length=256, blank=True, null=True)
    prolong_messaged = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s for %s per share / %s" % (
            self.shares, self.price, self.company.title
        )

    def history_dict(self):
        result = {
            'business': self.company.title,
            'listing_type': self.listing_type,
            'shares': self.shares,
            'price': unicode(self.price),
            'date': self.closedon.strftime('%d/%m/%y') if self.closedon else ''
        }
        return result