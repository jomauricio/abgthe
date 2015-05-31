# -*- coding: utf-8 -*-
from django.contrib import admin
#from ajax_select import make_ajax_form
#from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline, AjaxSelectAdminStackedInline
from .models import Game, Expansion
from .forms import GamesForm, ExpansionsForm


class ExpansionInline(admin.StackedInline):
	model = Expansion
	form = ExpansionsForm
	extra = 0

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	model = Game
	form = GamesForm
	inlines = [ExpansionInline]