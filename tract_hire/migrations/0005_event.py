# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-06 08:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tract_hire', '0004_tractor_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('tractor_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tract_hire.Tractor')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]