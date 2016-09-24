# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_ventaja_competitiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='img_obj1',
            field=models.ImageField(default='empresa/empresa/logo_mandaditho.jpg', upload_to=b'empresa/objetivos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='img_obj2',
            field=models.ImageField(default='empresa/empresa/logo_mandaditho.jpg', upload_to=b'empresa/objetivos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='img_obj3',
            field=models.ImageField(default='empresa/empresa/logo_mandaditho.jpg', upload_to=b'empresa/objetivos'),
            preserve_default=False,
        ),
    ]
