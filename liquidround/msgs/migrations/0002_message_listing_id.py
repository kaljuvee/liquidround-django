# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20150730_0821'),
        ('msgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='listing_id',
            field=models.ForeignKey(related_name='messages', blank=True, to='listings.Listing', null=True),
        ),
    ]
