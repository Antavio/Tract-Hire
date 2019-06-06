# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-06 16:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tract_hire', '0007_auto_20190606_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='prof_pics/')),
                ('bio', models.TextField()),
                ('all_tractors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tract_hire.Tractor')),
                ('prof_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
