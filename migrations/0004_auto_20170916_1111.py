# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0003_auto_20170916_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trans_network',
            name='fek',
        ),
        migrations.AlterField(
            model_name='trans_network',
            name='armodiot',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trans_network',
            name='arth_num',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trans_network',
            name='nameeng',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trans_network',
            name='namegrk',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trans_network',
            name='other_name',
            field=models.CharField(max_length=200),
        ),
    ]
