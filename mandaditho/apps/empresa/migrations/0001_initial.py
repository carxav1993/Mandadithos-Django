# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres_apellidos', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=155)),
                ('mensaje', models.CharField(max_length=500)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('leido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to=b'empresa/empresa')),
                ('favicon', models.ImageField(upload_to=b'empresa/empresa')),
                ('mision', models.CharField(max_length=255)),
                ('img_mision', models.ImageField(upload_to=b'empresa/empresa')),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=155)),
                ('red_facebook', models.URLField()),
                ('red_twiiter', models.URLField()),
                ('red_instagram', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion_pequenia', models.CharField(max_length=255)),
                ('descripcion_grande', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='telefonos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=155)),
            ],
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(to='empresa.Tipo_servicio'),
        ),
    ]
