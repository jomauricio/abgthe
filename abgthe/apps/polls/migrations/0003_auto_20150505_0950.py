# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150422_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseranking',
            name='accept',
            field=models.NullBooleanField(default=False, verbose_name=b'Concorda'),
            preserve_default=True,
        ),
    ]
