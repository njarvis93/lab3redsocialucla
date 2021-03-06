# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-11 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import red.models


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0003_auto_20170208_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador', to='red.Usuario', unique=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='red.Usuario'),
        ),
        migrations.AlterField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, upload_to=red.models.user_directory_path_audio),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='red.Usuario'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagenes',
            field=models.ImageField(blank=True, upload_to=red.models.user_directory_path_images),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, upload_to=red.models.user_directory_path_videos),
        ),
    ]
