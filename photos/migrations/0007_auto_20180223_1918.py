# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20180223_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
