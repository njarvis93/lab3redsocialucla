# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-29 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0023_auto_20170328_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(default='cedulax', max_length=8),
            preserve_default=False,
        ),
    ]
