# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20150421_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expansion',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='game',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='expansion',
            name='image',
            field=models.ImageField(null=True, upload_to=b'expansoes/image/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to=b'games/image/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
