# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_photo'),
        ('accounts', '0002_auto_20150723_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shares', models.PositiveIntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('listing_type', models.CharField(default=b'equity', max_length=15, choices=[(b'equity', b'Equity'), (b'offer', b'Offer')])),
                ('company', models.ForeignKey(related_name='listings', to='companies.Company')),
                ('user', models.ForeignKey(related_name='listings', to='accounts.Profile')),
            ],
        ),
    ]
