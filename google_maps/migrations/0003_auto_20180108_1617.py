# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('google_maps', '0002_auto_20180108_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datevisited',
            name='date_visited',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
