# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0013_auto_20170920_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eparxiako_odiko_diktio',
            name='geom',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=2100),
        ),
    ]
