from django.db import models
from django.utils import timezone
# Create your models here.

#from accounts.models import Profile

class Message(models.Model):
    user_from = models.ForeignKey('accounts.Profile', related_name='msgs_from', on_delete=models.CASCADE)
    user_to = models.ForeignKey('accounts.Profile', related_name='msgs_to', on_delete=models.CASCADE)
    subject = models.CharField(max_length=128)
    text = models.TextField(max_length=4000)
    createdon = models.DateTimeField(default=timezone.now)
    new = models.BooleanField(default=False)
    listing = models.ForeignKey('listings.Listing', related_name='messages', null=True, blank=True, on_delete=models.SET_NULL)

