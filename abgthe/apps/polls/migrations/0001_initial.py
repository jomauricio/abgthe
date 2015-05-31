# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0004_auto_20150421_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('create_user', models.ForeignKey(related_name='user_itens', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario')),
                ('game', models.ForeignKey(related_name='game_itens', verbose_name=b'Jogo', to='games.Game')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'aberta', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'aberta', b'aberta'), (b'fechada', b'fechada')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('description', models.CharField(max_length=200, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('initial_date', models.DateField(max_length=10, verbose_name=b'Data inicial')),
                ('final_date', models.DateField(max_length=10, verbose_name=b'Data final', blank=True)),
                ('poll_type', models.CharField(default=b'sixlistpoll', max_length=20, verbose_name=b'Tipo', choices=[(b'sixlistpoll', 'Lista Sextupla'), (b'purchasepoll', 'Compra')])),
                ('extraordinary', models.BooleanField(verbose_name=b'Extraordinaria')),
                ('create_user', models.ForeignKey(related_name='user_polls', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario')),
            ],
            options={
                'verbose_name': 'Vota\xe7\xe3o',
                'verbose_name_plural': 'Vota\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PurchaseRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('accept', models.BooleanField(default=False, verbose_name=b'Concorda')),
                ('create_user', models.ForeignKey(related_name='polls_purchaseranking_rakings', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario')),
                ('item', models.ForeignKey(related_name='polls_purchaseranking_rakings', verbose_name=b'Item', to='polls.Item')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Posi\xe7\xe3o',
                'verbose_name_plural': 'Posi\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SixListRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('ranking', models.SmallIntegerField(verbose_name=b'Ranking')),
                ('create_user', models.ForeignKey(related_name='polls_sixlistranking_rakings', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario')),
                ('item', models.ForeignKey(related_name='polls_sixlistranking_rakings', verbose_name=b'Item', to='polls.Item')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Posi\xe7\xe3o',
                'verbose_name_plural': 'Posi\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='poll',
            field=models.ForeignKey(related_name='poll_itens', verbose_name=b'Vota\xc3\xa7\xc3\xa3o', to='polls.Poll'),
            preserve_default=True,
        ),
    ]
