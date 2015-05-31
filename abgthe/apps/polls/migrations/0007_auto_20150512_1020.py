# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150509_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_user',
            field=models.ForeignKey(related_name='user_itens', verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='poll',
            field=models.ForeignKey(related_name='poll_itens', verbose_name=b'Vota\xc3\xa7\xc3\xa3o', to='polls.Poll'),
            preserve_default=True,
        ),
    ]
