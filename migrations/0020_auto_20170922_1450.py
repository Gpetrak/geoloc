# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0019_auto_20170922_1136'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='eparxiakoodikodiktio',
            table='eparxiako_odiko_diktio',
        ),
    ]
