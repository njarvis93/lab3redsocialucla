# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-12 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0008_auto_20170212_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='idiomas',
            field=models.ManyToManyField(blank=True, related_name='idiomas', to='red.Idioma'),
        ),
    ]
