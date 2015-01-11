# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EEtabel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summoners',
            name='Rank',
        ),
        migrations.AlterField(
            model_name='summoners',
            name='Summoner_name',
            field=models.CharField(unique=True, max_length=25),
        ),
    ]
