# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'Primeiro nome', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Segundo nome', blank=True)),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('birthday', models.DateField(max_length=100, null=True, verbose_name=b'Nascimento', blank=True)),
                ('gender', models.CharField(blank=True, max_length=20, verbose_name=b'Sexo', choices=[(b'male', 'Masculino'), (b'female', 'Feminino')])),
                ('cep', models.CharField(max_length=10, verbose_name=b'CEP', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'Endere\xc3\xa7o', blank=True)),
                ('cel_phone', models.CharField(max_length=15, verbose_name=b'Celular', blank=True)),
                ('home_phone', models.CharField(max_length=15, verbose_name=b'Fixo', blank=True)),
                ('state', models.CharField(blank=True, max_length=30, verbose_name=b'Estado', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('city', models.CharField(max_length=100, verbose_name=b'Cidade', blank=True)),
                ('username', models.CharField(verbose_name=b'username', unique=True, max_length=30, editable=False)),
                ('user', models.OneToOneField(related_name='profile', editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
            bases=(models.Model,),
        ),
    ]
