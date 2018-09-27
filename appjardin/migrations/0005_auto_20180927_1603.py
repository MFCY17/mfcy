# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appjardin', '0004_auto_20180927_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='date_joined',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
