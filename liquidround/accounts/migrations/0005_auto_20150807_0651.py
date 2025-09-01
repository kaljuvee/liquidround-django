# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='new',
        ),
        migrations.AddField(
            model_name='notification',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
