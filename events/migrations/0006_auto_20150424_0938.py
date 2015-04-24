# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150424_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fb_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
