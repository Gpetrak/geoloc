# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0006_loc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='trans_network',
        ),
    ]
