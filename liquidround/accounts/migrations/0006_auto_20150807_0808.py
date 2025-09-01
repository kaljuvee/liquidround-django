# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20150730_0821'),
        ('accounts', '0005_auto_20150807_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='listing_type',
        ),
        migrations.AddField(
            model_name='notification',
            name='listing',
            field=models.ForeignKey(default=1, to='listings.Listing'),
            preserve_default=False,
        ),
    ]
