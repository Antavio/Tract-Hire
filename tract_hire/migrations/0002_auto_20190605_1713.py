# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-05 17:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tract_hire', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tractor',
            old_name='location',
            new_name='location_id',
        ),
    ]