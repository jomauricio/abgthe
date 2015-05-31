# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices
from django.core.urlresolvers import reverse
from apps.games.models import Game


class Poll(TimeStampedModel, StatusModel):

	STATUS = Choices('aberta', 'ranqueamento', 'fechada', 'suspensa', )
	POLL_TYPE = Choices(('sixlistpoll', _('Lista Sextupla')), ('purchasepoll', _('Compra')))

	class Meta():
		verbose_name = "Votação"
		verbose_name_plural ="Votações"

	description = models.CharField("Descrição", max_length=200)
	initial_date = models.DateField("Data de abertura", max_length=10)
	ranking_date = models.DateField("Inicio do ranqueamento", max_length=10, blank=True, null=True)
	final_date = models.DateField("Data de fechamento", max_length=10, blank=True, null=True)
	poll_type = models.CharField("Tipo", choices=POLL_TYPE, max_length=20, default=POLL_TYPE.sixlistpoll)
	extraordinary = models.BooleanField("Extraordinaria", default=False)
	create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name='user_polls')

	def __unicode__(self):
		return u'%d :%s - %s' % (self.pk, self.description, self.poll_type)

	def get_absolute_url(self):
		if self.poll_type == self.POLL_TYPE.sixlistpoll:
			return reverse('polls:poll_sixlist_detail', kwargs={'pk': self.pk})
		else:
			return reverse('polls:poll_purchase_detail', kwargs={'pk': self.pk})

	def accept(self):
		
		accepts = self.poll_purchaseaccepts.all()
		yes = accepts.filter(accept=True).count()
		no = accepts.filter(accept=False).count()
	
		if self.poll_type == 'purchasepoll':
			if yes>no:
				return True
			else:
				return False
		else:
			return False	

class Item(TimeStampedModel):

	class Meta():
		verbose_name = "Item"
		verbose_name_plural ="Itens"
		unique_together = ("poll", "game")

	poll = models.ForeignKey(Poll, verbose_name="Votação", related_name="poll_itens")
	game = models.ForeignKey(Game, verbose_name="Jogo", related_name="game_itens")
	create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name="user_itens")

	def __unicode__(self):
		return u'Item cod: %s - Jogo: %s' % (str(self.pk), self.game.name)

	def parcial(self):
		
		total = 0
		
		if self.poll.poll_type == self.poll.POLL_TYPE.sixlistpoll:
			rankings = self.sixlistranking_rankings.all()
			for ranking in rankings:
				total += ranking.ranking

		return total


class SixListRanking(TimeStampedModel):

	class Meta():
		verbose_name = "Posição"
		verbose_name_plural ="Posições"
		unique_together = ("item", "create_user")

	
	item = models.ForeignKey(Item, verbose_name="Item", related_name="sixlistranking_rankings")
	create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name="user_rakings", editable=False)
	ranking = models.SmallIntegerField("Ranking",null=True,blank=True)

	def __unicode__(self):
		return u'Ranking cod: %s' % (str(self.pk))

	def get_absolute_url(self):
		pass #return reverse('games:game_detail', args=[self.slug])


class PurchaseAccept(TimeStampedModel):

	class Meta():
		verbose_name = "Aceitação"
		verbose_name_plural ="Aceitações"
		unique_together = ("poll", "create_user")	

	poll = models.ForeignKey(Poll, verbose_name="Votação", related_name="poll_purchaseaccepts")
	create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name="user_accepts")
	accept = models.NullBooleanField("Concorda", default=False)