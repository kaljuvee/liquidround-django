# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0002_message_listing_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='listing_id',
            new_name='listing',
        ),
        migrations.AlterField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(related_name='msgs_from', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(related_name='msgs_to', to='accounts.Profile'),
        ),
    ]
