# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import autoslug.fields
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'Nome')),
                ('image', models.ImageField(null=True, upload_to=b'expansoes/image/%Y/%m/%d', blank=True)),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('number_players', models.CharField(max_length=10, verbose_name=b'N\xc2\xba de Jogadores', blank=True)),
            ],
            options={
                'verbose_name': 'Expans\xe3o',
                'verbose_name_plural': 'Expans\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'Nome')),
                ('image', models.ImageField(null=True, upload_to=b'games/image/%Y/%m/%d', blank=True)),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('number_players', models.CharField(max_length=10, verbose_name=b'N\xc2\xba de Jogadores', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Tags')),
            ],
            options={
                'verbose_name': 'Jogo',
                'verbose_name_plural': 'Jogos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expansion',
            name='game',
            field=models.ForeignKey(related_name='expansions', verbose_name=b'Jogo', to='games.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expansion',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Tags'),
            preserve_default=True,
        ),
    ]
