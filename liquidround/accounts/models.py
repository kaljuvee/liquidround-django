from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

from companies.models import Company

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Phone', max_length=30)

    CERTS = (
        ('hnwi', 'I certify that I am a High Net Worth Investor'),
        ('si', 'I certify that I am a qualified Sophisticated Investor'),
    )
    certified = models.CharField(
        'Certified', 
        max_length=10, 
        choices=CERTS,
        default='hnwi'
    )
    activationcode = models.CharField(max_length=255, blank=True, null=True)
    activatedon = models.DateTimeField(blank=True, null=True)
    watching = models.ManyToManyField(
        'companies.Company', 
        related_name='watching', 
        blank=True
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} / {self.user.email}'

    def watch(self, company_id):
        if self.watching.filter(pk=company_id).count() > 0:
            self.watching.remove(company_id)
            return 'unwatched'
        else:
            try:
                company = Company.objects.get(pk=company_id)
                self.watching.add(company)
                return 'watched'
            except Company.DoesNotExist:
                pass
        return False

class Notification(models.Model):
    user = models.ForeignKey(Profile, related_name='notifications', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)

