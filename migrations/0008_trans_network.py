# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0007_delete_trans_network'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trans_network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objectid', models.IntegerField()),
                ('typeid', models.FloatField()),
                ('namegrk', models.CharField(max_length=66)),
                ('nameeng', models.CharField(max_length=69)),
                ('length', models.FloatField()),
                ('armodiot', models.CharField(max_length=49)),
                ('arth_num', models.CharField(max_length=17)),
                ('other_name', models.CharField(max_length=69)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=2100)),
            ],
        ),
    ]
