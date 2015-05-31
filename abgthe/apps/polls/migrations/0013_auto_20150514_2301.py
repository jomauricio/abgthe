# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20150513_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='ranking_date',
            field=models.DateField(max_length=10, null=True, verbose_name=b'Inicio do ranqueamento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poll',
            name='final_date',
            field=models.DateField(max_length=10, null=True, verbose_name=b'Data de fechamento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poll',
            name='initial_date',
            field=models.DateField(max_length=10, verbose_name=b'Data de abertura'),
            preserve_default=True,
        ),
    ]
