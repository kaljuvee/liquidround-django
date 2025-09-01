# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'Company name')),
                ('website', models.URLField(verbose_name=b'Website')),
                ('industry', models.CharField(max_length=128, verbose_name=b'Industry')),
                ('role', models.CharField(max_length=256, verbose_name=b'Specific Role')),
                ('location', models.CharField(max_length=128, verbose_name=b'Location')),
            ],
        ),
    ]
