# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150505_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='final_date',
            field=models.DateField(max_length=10, null=True, verbose_name=b'Data final', blank=True),
            preserve_default=True,
        ),
    ]
