# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20141216_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='title',
            field=models.CharField(unique=True, max_length=25, error_messages={'unique': 'See nimi on juba lisatud.'}),
        ),
    ]
