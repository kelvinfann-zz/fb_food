# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_event_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor_name',
            new_name='name',
        ),
    ]
