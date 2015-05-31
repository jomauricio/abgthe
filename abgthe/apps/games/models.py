# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils import Choices
from localflavor.br.br_states import STATE_CHOICES
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Game(TimeStampedModel):

	class Meta():
		verbose_name = "Jogo"
		verbose_name_plural ="Jogos"

	slug = AutoSlugField(populate_from='name', unique=True)
	name = models.CharField("Nome", max_length=100, unique=True)
	image = ProcessedImageField(upload_to="games/image/%Y/%m/%d", blank=True, null=True,
		processors=[ResizeToFill(80, 90)], format='JPEG',options={'quality': 60})
	description = models.TextField("Descrição", blank=True)
	number_players = models.CharField("Nº de Jogadores", blank=True, max_length=10)
	tags = TaggableManager(verbose_name='Tags', blank=True)

	def __unicode__(self):
		return u'%s' % (self.name)

	def get_absolute_url(self):
		return reverse('games:game_detail', args=[self.slug])

class Expansion(TimeStampedModel):

	class Meta():
		verbose_name = "Expansão"
		verbose_name_plural ="Expansões"

	game = models.ForeignKey(Game, verbose_name="Jogo",related_name="expansions")
	slug = AutoSlugField(populate_from='name', unique=True)
	name = models.CharField("Nome", max_length=100, unique=True)
	image = ProcessedImageField(upload_to="games/image/%Y/%m/%d", blank=True, null=True,
		processors=[ResizeToFill(80, 90)], format='JPEG',options={'quality': 60})
	description = models.TextField("Descrição", blank=True)
	number_players = models.CharField("Nº de Jogadores", blank=True, max_length=10)
	tags = TaggableManager(verbose_name='Tags', blank=True)

	def __unicode__(self):
		return u'%s' % (self.name)

	def get_absolute_url(self):
		return reverse('games:expansion_detail', args=[self.slug])