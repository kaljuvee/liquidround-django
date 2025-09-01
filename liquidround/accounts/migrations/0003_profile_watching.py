# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_published'),
        ('accounts', '0002_auto_20150723_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='watching',
            field=models.ManyToManyField(related_name='watching', to='companies.Company', blank=True),
        ),
    ]
