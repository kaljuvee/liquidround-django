from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from redactor.fields import RedactorField
from django.utils import timezone


class News(models.Model):
    title = models.CharField('Title', max_length=128)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=True)
    text = RedactorField(upload_to='pages/', max_length=4294967295, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self):
        if self.slug == "":
            self.slug = slugify(self.title)
        return super(News, self).save()

    class Meta:
        ordering = ['-date']