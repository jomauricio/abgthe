# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150421_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(max_length=10, null=True, verbose_name=b'Nascimento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=20, verbose_name=b'Sexo', choices=[(b'masculino', 'Masculino'), (b'feminino', 'Feminino')]),
            preserve_default=True,
        ),
    ]
