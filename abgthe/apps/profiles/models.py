# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils import Choices
from localflavor.br.br_states import STATE_CHOICES
from django.core.urlresolvers import reverse
from allauth.socialaccount.models import SocialAccount
from allauth.account.signals import user_signed_up
from django.core.files import File
from avatar.models import Avatar
from urllib2 import urlopen
import requests
from django.core.files.temp import NamedTemporaryFile


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

	def download_avatar(self, url):
		"""
		"""
		r = requests.get(url)

		img_temp = NamedTemporaryFile(delete=True)
		img_temp.write(r.content)
		img_temp.flush()
		img_temp.seek(0)
		return File(img_temp)

	@receiver(user_signed_up)
	def user_signed_up_(request, user, sociallogin=None, **kwargs):
		'''
		When a social account is created successfully and this signal is received,
		django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:

		sociallogin.account.provider  # e.g. 'twitter'
		sociallogin.account.get_avatar_url()
		sociallogin.account.get_profile_url()
		sociallogin.account.extra_data['screen_name']

		See the socialaccount_socialaccount table for more in the 'extra_data' field.
		'''

		if sociallogin:
		# Extract first / last names from social nets and store on Profile record
			if sociallogin.account.provider == 'facebook':
				user.profile.first_name = sociallogin.account.extra_data['first_name']
				user.profile.last_name = sociallogin.account.extra_data['last_name']

			if sociallogin.account.provider == 'google':
				user.profile.first_name = sociallogin.account.extra_data['given_name']
				user.profile.last_name = sociallogin.account.extra_data['family_name']
		
			user.profile.save()
		
			mage_avatar = user.profile.download_avatar(sociallogin.account.get_avatar_url())
			avatar = Avatar(user=user,primary=True, avatar=image_avatar)
			avatar.save()