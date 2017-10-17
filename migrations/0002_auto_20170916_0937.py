# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trans_network',
            old_name='nameeng',
            new_name='name',
        ),
    ]
