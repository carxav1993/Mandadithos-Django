# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0008_auto_20160722_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locales',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='locales',
            name='referencias',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
    ]
