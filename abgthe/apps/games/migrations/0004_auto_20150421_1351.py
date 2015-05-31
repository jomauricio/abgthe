# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20150421_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expansion',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'games/image/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'games/image/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
