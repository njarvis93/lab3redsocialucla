# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-12 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('red', '0005_auto_20170211_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='intereses',
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='id_autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencia', to='red.Perfil'),
        ),
        migrations.AlterField(
            model_name='nivelformacion',
            name='fecha_finalizacion',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='nivelformacion',
            name='id_autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formacion', to='red.Perfil'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='idiomas',
            field=models.ManyToManyField(blank=True, to='red.Idioma'),
        ),
        migrations.AddField(
            model_name='interes',
            name='id_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intereses', to='red.Perfil'),
        ),
    ]
