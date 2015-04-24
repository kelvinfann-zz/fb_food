# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150423_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'end time of event'),
        ),
        migrations.AddField(
            model_name='event',
            name='fb_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'start of event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
