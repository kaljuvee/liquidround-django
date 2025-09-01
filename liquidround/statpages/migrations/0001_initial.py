# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=4294967295L, null=True, blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('top_menu', models.BooleanField(default=False)),
            ],
        ),
    ]
