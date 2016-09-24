# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0011_auto_20160809_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='favicon',
            field=models.ImageField(default='imagen_aqui', upload_to=b'empresa/empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_mision',
            field=models.ImageField(default='imagenaqui', upload_to=b'empresa/empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_obj1',
            field=models.ImageField(default='imagenaqui', upload_to=b'empresa/objetivos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_obj2',
            field=models.ImageField(default='imagenaqui', upload_to=b'empresa/objetivos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_obj3',
            field=models.ImageField(default='imagenaqui', upload_to=b'empresa/objetivos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(default='imagenaqui', upload_to=b'empresa/empresa'),
            preserve_default=False,
        ),
    ]
