# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-06 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tract_hire', '0005_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
