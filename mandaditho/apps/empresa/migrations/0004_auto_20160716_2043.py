# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20160716_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
