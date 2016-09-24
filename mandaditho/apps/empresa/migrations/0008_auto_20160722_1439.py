# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0007_auto_20160717_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='locales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=15)),
                ('provincia', models.CharField(max_length=50, choices=[(b'AZ', b'Azuay'), (b'BO', b'Bolivar'), (b'CA', b'Ca\xc3\xb1ar'), (b'CR', b'Carchi'), (b'CH', b'Chimborazo'), (b'CO', b'Cotopaxi'), (b'OR', b'El Oro'), (b'ES', b'Esmeraldas'), (b'GA', b'Gal\xc3\xa1pagos'), (b'GU', b'Guayas'), (b'IM', b'Imbabura'), (b'LO', b'Loja'), (b'LR', b'Los Rios'), (b'MA', b'Manabi'), (b'MS', b'Morona Santiago'), (b'NA', b'Napo'), (b'OR', b'Orellana'), (b'PA', b'Pastaza'), (b'PI', b'Pichincha'), (b'SE', b'Santa Elena'), (b'SD', b'Santo Domingo'), (b'SU', b'Sucumbios'), (b'TU', b'Tungurahua'), (b'ZA', b'Zamora')])),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('referencias', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('convencional1', models.CharField(max_length=15, null=True, blank=True)),
                ('convencional2', models.CharField(max_length=15, null=True, blank=True)),
                ('celular1', models.CharField(max_length=10)),
                ('celular2', models.CharField(max_length=10, null=True, blank=True)),
                ('mensaje', models.TextField()),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='trabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
                ('convencional', models.CharField(max_length=15, null=True, blank=True)),
                ('celular', models.CharField(max_length=10)),
                ('provincia', models.CharField(max_length=50, choices=[(b'AZ', b'Azuay'), (b'BO', b'Bolivar'), (b'CA', b'Ca\xc3\xb1ar'), (b'CR', b'Carchi'), (b'CH', b'Chimborazo'), (b'CO', b'Cotopaxi'), (b'OR', b'El Oro'), (b'ES', b'Esmeraldas'), (b'GA', b'Gal\xc3\xa1pagos'), (b'GU', b'Guayas'), (b'IM', b'Imbabura'), (b'LO', b'Loja'), (b'LR', b'Los Rios'), (b'MA', b'Manabi'), (b'MS', b'Morona Santiago'), (b'NA', b'Napo'), (b'OR', b'Orellana'), (b'PA', b'Pastaza'), (b'PI', b'Pichincha'), (b'SE', b'Santa Elena'), (b'SD', b'Santo Domingo'), (b'SU', b'Sucumbios'), (b'TU', b'Tungurahua'), (b'ZA', b'Zamora')])),
                ('ciudad', models.CharField(max_length=75)),
                ('estado_civil', models.CharField(max_length=50, choices=[(b'SO', b'Soltero/a'), (b'CA', b'Casado/a'), (b'VI', b'Viudo/a'), (b'UN', b'Union Laboral')])),
                ('curriculum', models.FileField(upload_to=b'empresa/curriculums')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('revisado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='caracteristica_descripcion1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='caracteristica_descripcion2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='caracteristica_descripcion3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='caracteristica_descripcion4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='mision',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion_grande',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ventaja_competitiva',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
