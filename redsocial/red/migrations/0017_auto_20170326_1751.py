# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-26 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0016_auto_20170326_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=20000),
        ),
    ]