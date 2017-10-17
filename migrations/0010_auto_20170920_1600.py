# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0009_auto_20170920_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eparxiako_odiko_diktio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aa', models.IntegerField()),
                ('yparith', models.CharField(max_length=254)),
                ('onomasia', models.CharField(max_length=100)),
                ('katataksi', models.CharField(max_length=100)),
                ('tmima', models.CharField(max_length=50)),
                ('apallotr', models.CharField(max_length=100)),
                ('fekapall', models.CharField(max_length=50)),
                ('arfakellou', models.CharField(max_length=50)),
                ('sxolia', models.CharField(max_length=250)),
                ('parakatath', models.CharField(max_length=250)),
                ('yp', models.CharField(max_length=20)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=2100)),
            ],
        ),
        migrations.DeleteModel(
            name='Trans_network',
        ),
    ]
