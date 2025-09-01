# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='cloedon',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
