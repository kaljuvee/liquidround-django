# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_cloedon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='cloedon',
            new_name='closedon',
        ),
    ]
