# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_listing_expireson'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='prolong_code',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='prolong_messaged',
            field=models.BooleanField(default=False),
        ),
    ]
