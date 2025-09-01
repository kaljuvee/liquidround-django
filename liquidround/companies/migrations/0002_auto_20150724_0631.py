# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='location',
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=30, null=True, verbose_name=b'City', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='class_a',
            field=models.BooleanField(default=False, verbose_name=b'Share Class A'),
        ),
        migrations.AddField(
            model_name='company',
            name='class_b',
            field=models.BooleanField(default=False, verbose_name=b'Share Class B'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Country', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='funding_stage',
            field=models.CharField(default=b'', choices=[(b'series_a', b'Series A'), (b'series_b', b'Series B'), (b'series_c', b'Series C')], max_length=30, blank=True, null=True, verbose_name=b'Current Funding State'),
        ),
        migrations.AddField(
            model_name='company',
            name='pre_emption_rights',
            field=models.BooleanField(default=False, verbose_name=b'Pre-emption Rights'),
        ),
        migrations.AddField(
            model_name='company',
            name='summary',
            field=models.TextField(max_length=40000, null=True, verbose_name=b'Business Summary', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='voting_rights',
            field=models.BooleanField(default=False, verbose_name=b'Voting Rights'),
        ),
    ]
