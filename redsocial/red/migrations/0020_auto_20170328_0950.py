# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-28 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0019_auto_20170327_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]