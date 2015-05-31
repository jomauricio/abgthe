# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150508_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='poll',
            field=models.ForeignKey(related_name='poll_itens', editable=False, to='polls.Poll', verbose_name=b'Vota\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchaseranking',
            name='item',
            field=models.ForeignKey(related_name='polls_purchaseranking_rankings', verbose_name=b'Item', to='polls.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sixlistranking',
            name='item',
            field=models.ForeignKey(related_name='polls_sixlistranking_rankings', verbose_name=b'Item', to='polls.Item'),
            preserve_default=True,
        ),
    ]
