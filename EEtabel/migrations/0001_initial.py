# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summoners',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Rank', models.CharField(max_length=5)),
                ('Summoner_name', models.CharField(max_length=25)),
                ('League', models.CharField(max_length=15)),
                ('Division', models.CharField(max_length=3)),
                ('League_points', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
