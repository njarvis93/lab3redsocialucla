# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-11 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0004_auto_20170211_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ocurrencia', models.DateField()),
                ('hora_ocurrencia', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='red.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='actividad',
            name='id_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividad', to='red.Post'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id_actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='red.Actividad'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id_comentario_padre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='red.Comentario'),
        ),
        migrations.AlterField(
            model_name='compartir',
            name='id_actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to='red.Actividad'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id_canal',
            field=models.ManyToManyField(blank=True, related_name='posts', to='red.Canal'),
        ),
        migrations.AddField(
            model_name='likes',
            name='id_actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me_gustas', to='red.Actividad'),
        ),
    ]
