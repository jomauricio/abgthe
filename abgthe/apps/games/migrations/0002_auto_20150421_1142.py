# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expansion',
            name='image',
        ),
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.AddField(
            model_name='expansion',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'games/image/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'games/image/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
