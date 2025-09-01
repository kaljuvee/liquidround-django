# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='team_desc',
            field=models.TextField(max_length=40000, null=True, verbose_name=b'Team Description', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(null=True, verbose_name=b'Slug', blank=True),
        ),
    ]
