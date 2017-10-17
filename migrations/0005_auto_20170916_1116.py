# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0004_auto_20170916_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trans_network',
            name='lstring',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
        ),
    ]
