# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20150724_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Document Title')),
                ('doc', models.FileField(upload_to=b'attach', verbose_name=b'File')),
                ('company', models.ForeignKey(related_name='documents', to='companies.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'Member, Occupation')),
                ('company', models.ForeignKey(related_name='team', to='companies.Company')),
            ],
        ),
    ]
