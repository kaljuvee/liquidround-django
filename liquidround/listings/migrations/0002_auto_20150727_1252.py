# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='approvedon',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='createdon',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='listing',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
