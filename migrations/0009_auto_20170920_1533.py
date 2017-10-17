# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0008_trans_network'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trans_network',
            name='other_name',
            field=models.CharField(max_length=100),
        ),
    ]
