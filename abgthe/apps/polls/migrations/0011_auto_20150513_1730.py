# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20150513_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sixlistranking',
            name='ranking',
            field=models.SmallIntegerField(null=True, verbose_name=b'Ranking'),
            preserve_default=True,
        ),
    ]
