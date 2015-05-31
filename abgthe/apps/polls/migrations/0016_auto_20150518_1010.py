# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20150516_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseaccept',
            name='create_user',
            field=models.ForeignKey(related_name='user_accepts', verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
