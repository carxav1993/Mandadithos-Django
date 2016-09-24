# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20160716_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetivo',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion_grande',
            field=models.CharField(max_length=500),
        ),
    ]
