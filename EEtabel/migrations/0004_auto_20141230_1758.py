# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EEtabel', '0003_auto_20141228_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='summoners',
            name='Rank',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='summoners',
            name='Summoner_name',
            field=models.CharField(max_length=25),
        ),
    ]
