# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_activatedon'),
        ('companies', '0007_company_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uploadedby',
            field=models.ForeignKey(to='accounts.Profile', null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='uploadedon',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
