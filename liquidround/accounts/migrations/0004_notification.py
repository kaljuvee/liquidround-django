# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_published'),
        ('accounts', '0003_profile_watching'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdon', models.DateTimeField(default=django.utils.timezone.now)),
                ('listing_type', models.CharField(max_length=30)),
                ('new', models.BooleanField(default=True)),
                ('company', models.ForeignKey(related_name='notifications', to='companies.Company')),
                ('user', models.ForeignKey(related_name='notifications', to='accounts.Profile')),
            ],
        ),
    ]
