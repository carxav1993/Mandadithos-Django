# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, choices=[(b'cn', b'Convencional'), (b'cl', b'Celular')])),
                ('operadora', models.CharField(max_length=50, choices=[(b'CL', b'Claro'), (b'MO', b'Movistar'), (b'CNT', b'CNT'), (b'TW', b'Tuenti')])),
                ('numero', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='telefonos',
        ),
        migrations.AddField(
            model_name='objetivo',
            name='tipo',
            field=models.CharField(default=datetime.datetime(2016, 7, 16, 22, 12, 31, 988000, tzinfo=utc), max_length=50, choices=[(b'LP', b'Largo Plazo'), (b'MP', b'Mediano Plazo'), (b'CP', b'Corto Plazo')]),
            preserve_default=False,
        ),
    ]
