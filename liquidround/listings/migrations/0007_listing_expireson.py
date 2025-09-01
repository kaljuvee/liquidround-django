# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20150730_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='expireson',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
