# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appjardin', '0003_auto_20180927_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='cedula',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='genero',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
