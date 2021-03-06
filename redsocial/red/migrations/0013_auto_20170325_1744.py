# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-25 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0012_auto_20170319_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador', to='red.Usuario'),
        ),
        migrations.AlterField(
            model_name='canal',
            name='fecha_creacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='canal',
            name='miembros',
            field=models.ManyToManyField(blank=True, to='red.Perfil'),
        ),
    ]
