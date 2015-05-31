# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0014_auto_20150514_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseAccept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('accept', models.NullBooleanField(default=False, verbose_name=b'Concorda')),
                ('create_user', models.ForeignKey(related_name='user_accepts', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario')),
                ('poll', models.ForeignKey(related_name='poll_purchaseaccepts', verbose_name=b'Vota\xc3\xa7\xc3\xa3o', to='polls.Poll')),
            ],
            options={
                'verbose_name': 'Aceita\xe7\xe3o',
                'verbose_name_plural': 'Aceita\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='purchaseranking',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='purchaseranking',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='purchaseranking',
            name='item',
        ),
        migrations.DeleteModel(
            name='PurchaseRanking',
        ),
        migrations.AlterUniqueTogether(
            name='purchaseaccept',
            unique_together=set([('poll', 'create_user')]),
        ),
        migrations.AlterField(
            model_name='sixlistranking',
            name='create_user',
            field=models.ForeignKey(related_name='user_rakings', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario'),
            preserve_default=True,
        ),
    ]
