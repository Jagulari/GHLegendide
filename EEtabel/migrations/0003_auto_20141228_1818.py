# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EEtabel', '0002_auto_20141217_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summoners',
            name='Division',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='summoners',
            name='League',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='summoners',
            name='League_points',
            field=models.CharField(max_length=5),
        ),
    ]
