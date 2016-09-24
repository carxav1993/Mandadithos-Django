# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0010_remove_locales_ruc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='favicon',
            field=models.ImageField(null=True, upload_to=b'empresa/empresa', blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_mision',
            field=models.ImageField(null=True, upload_to=b'empresa/empresa', blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_obj1',
            field=models.ImageField(null=True, upload_to=b'empresa/objetivos', blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_obj2',
            field=models.ImageField(null=True, upload_to=b'empresa/objetivos', blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='img_obj3',
            field=models.ImageField(null=True, upload_to=b'empresa/objetivos', blank=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'empresa/empresa', blank=True),
        ),
    ]
