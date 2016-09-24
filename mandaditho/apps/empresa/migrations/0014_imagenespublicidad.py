# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0013_servicio_img_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesPublicidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'empresa/publicidad')),
            ],
        ),
    ]
