# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_auto_20160716_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventaja_Competitiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
    ]
