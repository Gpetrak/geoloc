# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trans_network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objectid', models.IntegerField()),
                ('typeid', models.FloatField()),
                ('namegrk', models.CharField(max_length=20)),
                ('nameeng', models.CharField(max_length=20)),
                ('length', models.FloatField()),
                ('armodiot', models.CharField(max_length=20)),
                ('arth_num', models.CharField(max_length=20)),
                ('other_name', models.CharField(max_length=20)),
                ('fek', models.CharField(max_length=10)),
                ('lstring', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
    ]
