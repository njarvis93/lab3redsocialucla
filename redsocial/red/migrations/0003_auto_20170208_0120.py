# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-08 05:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0002_auto_20170207_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['fecha_creacion', 'hora_creacion']},
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='autor_actividad',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='fecha_ocurrencia',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='hora_ocurrencia',
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='red.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha_ocurrencia',
            field=models.DateField(default=datetime.date(2017, 2, 8)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compartir',
            name='autor',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='red.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compartir',
            name='fecha_ocurrencia',
            field=models.DateField(default=datetime.date(2017, 2, 8)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('autor', 'fecha_creacion', 'hora_creacion')]),
        ),
    ]
