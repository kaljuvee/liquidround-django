# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activationcode',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='certified',
            field=models.CharField(default=b'hnwi', max_length=10, verbose_name=b'Certified', choices=[(b'hnwi', b'I certify that I am a High Net Worth Investor'), (b'si', b'I certify that I am a qualified Sophisticated Investor')]),
        ),
    ]
