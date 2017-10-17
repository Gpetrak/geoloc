# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0002_auto_20170916_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trans_network',
            old_name='name',
            new_name='nameeng',
        ),
    ]
