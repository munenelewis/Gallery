# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20180225_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]
