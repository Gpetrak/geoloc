# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0020_auto_20170922_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdikoDiktyoKritis',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('objectid', models.IntegerField(null=True, blank=True)),
                ('type', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('namegrk', models.CharField(max_length=66, null=True, blank=True)),
                ('nameeng', models.CharField(max_length=69, null=True, blank=True)),
                ('length', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('armodiot', models.CharField(max_length=49, null=True, blank=True)),
                ('arth_num', models.CharField(max_length=33, null=True, blank=True)),
                ('other_name', models.CharField(max_length=123, null=True, blank=True)),
                ('fek', models.CharField(max_length=25, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=2100, null=True, blank=True)),
            ],
            options={
                'db_table': 'odiko_diktyo_kritis',
                'managed': False,
            },
        ),
    ]
