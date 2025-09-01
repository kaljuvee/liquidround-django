# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
