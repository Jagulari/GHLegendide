# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=25),
        ),
    ]
