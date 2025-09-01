from django.db import models

# Create your models here.
from django.utils import timezone


class CompanyRequest(models.Model):
    url = models.URLField()
    createdon = models.DateTimeField(default=timezone.now)
    updatedon = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.url