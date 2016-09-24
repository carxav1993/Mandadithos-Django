# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20160716_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='caracteristica1',
            field=models.CharField(default='caracteristica1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica2',
            field=models.CharField(default='caracteristica2', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica3',
            field=models.CharField(default='caracteristica3', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica4',
            field=models.CharField(default='caracteristica4', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica_descripcion1',
            field=models.CharField(default='c1d', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica_descripcion2',
            field=models.CharField(default='c2d', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica_descripcion3',
            field=models.CharField(default='c3d', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='caracteristica_descripcion4',
            field=models.CharField(default='c4d', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='telefono',
            name='tipo',
            field=models.CharField(max_length=50, choices=[(b'CN', b'Convencional'), (b'CL', b'Celular')]),
        ),
    ]
