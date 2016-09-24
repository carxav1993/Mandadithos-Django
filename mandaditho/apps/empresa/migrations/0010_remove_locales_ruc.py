# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0009_auto_20160723_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locales',
            name='ruc',
        ),
    ]
