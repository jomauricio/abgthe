# -*- coding: utf-8 -*-
from django.contrib import admin
#from ajax_select import make_ajax_form
#from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline, AjaxSelectAdminStackedInline
from .models import Poll, Item, SixListRanking, PurchaseAccept
#from .forms import PollSixListForm, PollPurchaseForm


class ItemInline(admin.StackedInline):
	model = Item
	extra = 0

	def save_model(self, request, obj, form, change):
		obj.create_user = request.user
		obj.save()


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
	model = Poll
	exclude = ('create_user',)
	#inlines = [ItemInline,]

	def save_model(self, request, obj, form, change):
		if not change:
			obj.create_user = request.user
			obj.save()
		else:
			obj.save()

	'''def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		for obj in formset.deleted_objects:
			obj.delete()
		for instance in instances:
			instance.create_user = request.user
			instance.save()
		formset.save_m2m()'''

@admin.register(SixListRanking)
class SixListRankingAdmin(admin.ModelAdmin):
	model = SixListRanking

	def save_model(self, request, obj, form, change):
		obj.create_user = request.user
		obj.save()