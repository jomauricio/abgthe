# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20150514_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='create_user',
            field=models.ForeignKey(related_name='user_polls', verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
