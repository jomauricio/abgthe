# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils import Choices
from localflavor.br.br_states import STATE_CHOICES
from django.core.urlresolvers import reverse

class Profile(TimeStampedModel):
	
	class Meta():
		verbose_name = "Perfil"
		verbose_name_plural ="Perfis"
	
	GENDER = Choices(('masculino', _('Masculino')), ('feminino', _('Feminino')))

	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name="profile", editable=False)
	first_name = models.CharField("Primeiro nome", max_length=30, blank=True)
	last_name = models.CharField("Segundo nome", max_length=30, blank=True)
	description = models.TextField("Descrição", blank=True)
	birthday = models.DateField("Nascimento", max_length=10, blank=True, null=True)
	gender = models.CharField("Sexo", choices=GENDER, max_length=20, blank=True)
	cep = models.CharField("CEP", max_length=10, blank=True)
	address = models.CharField("Endereço", max_length=200, blank=True)
	cel_phone = models.CharField("Celular", max_length=15, blank=True)
	home_phone = models.CharField("Fixo", max_length=15, blank=True)
	state = models.CharField("Estado", choices=STATE_CHOICES, max_length=30, blank=True)
	city = models.CharField("Cidade", max_length=100, blank=True)
	username = models.CharField("username", unique=True, max_length=30, editable=False)

	def __unicode__(self):
		if self.first_name and self.last_name:
			return u'%s %s' % (self.first_name, self.last_name)
		else:
			return self.username

	def get_absolute_url(self):
		return reverse('profiles:profile_detail', args=[self.username])

	def save(self, *args, **kwargs):
		u = self.user
		u.first_name = self.first_name
		u.last_name = self.last_name
		u.save()
		self.user = u
		super(Profile, self).save(*args, **kwargs)
