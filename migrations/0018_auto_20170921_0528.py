# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0017_auto_20170921_0458'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eparxiako_odiko_diktio',
            new_name='EparxiakoOdikoDiktio',
        ),
        migrations.AlterModelTable(
            name='eparxiakoodikodiktio',
            table='geoloc_eparxiako_odiko_diktio',
        ),
    ]
