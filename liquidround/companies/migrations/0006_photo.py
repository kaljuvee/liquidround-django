# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_document_teammate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'companies', verbose_name=b'Image')),
                ('is_main', models.BooleanField(default=False, verbose_name=b'Is main image?')),
                ('company', models.ForeignKey(related_name='photos', to='companies.Company')),
            ],
            options={
                'ordering': ['-is_main'],
            },
        ),
    ]
