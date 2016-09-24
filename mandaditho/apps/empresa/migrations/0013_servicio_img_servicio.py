# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0012_auto_20160809_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='img_servicio',
            field=models.ImageField(default='imagen', upload_to=b'empresa/servicios'),
            preserve_default=False,
        ),
    ]
