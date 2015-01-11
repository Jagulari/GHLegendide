# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EEtabel', '0004_auto_20141230_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summoners',
            name='Rank',
        ),
        migrations.AddField(
            model_name='summoners',
            name='TotalLP',
            field=models.PositiveIntegerField(editable=False, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='summoners',
            name='League_points',
            field=models.DecimalField(max_digits=3, decimal_places=0),
        ),
    ]
