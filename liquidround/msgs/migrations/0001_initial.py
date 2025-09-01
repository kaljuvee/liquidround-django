# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150723_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=4000)),
                ('createdon', models.DateTimeField(default=django.utils.timezone.now)),
                ('new', models.BooleanField(default=False)),
                ('user_from', models.ForeignKey(related_name='user_from', to='accounts.Profile')),
                ('user_to', models.ForeignKey(related_name='user_to', to='accounts.Profile')),
            ],
        ),
    ]
