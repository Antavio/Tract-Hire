# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-05 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tractor_image', models.ImageField(blank=True, upload_to='tractor_pics')),
                ('category', models.CharField(max_length=200)),
                ('price_estimate', models.FloatField()),
                ('contact', models.IntegerField()),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tract_hire.Location')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
