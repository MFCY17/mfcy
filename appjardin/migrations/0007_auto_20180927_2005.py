# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appjardin', '0006_auto_20180927_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
