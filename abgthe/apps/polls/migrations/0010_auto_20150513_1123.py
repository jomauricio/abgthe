# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20150512_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseranking',
            name='item',
            field=models.ForeignKey(related_name='purchaseranking_rankings', verbose_name=b'Item', to='polls.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sixlistranking',
            name='item',
            field=models.ForeignKey(related_name='sixlistranking_rankings', verbose_name=b'Item', to='polls.Item'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='purchaseranking',
            unique_together=set([('item', 'create_user')]),
        ),
        migrations.AlterUniqueTogether(
            name='sixlistranking',
            unique_together=set([('item', 'create_user')]),
        ),
    ]
