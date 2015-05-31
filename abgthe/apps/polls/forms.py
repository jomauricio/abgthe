# -*- coding: utf-8 -*-
#from django import forms
from .models import Item, Poll, PurchaseAccept
from ajax_select.fields import AutoCompleteSelectField
import floppyforms.__future__ as forms
from django.core.exceptions import NON_FIELD_ERRORS


class PollSixListForm(forms.ModelForm):

    class Meta:
        model = Poll
        exclude = ['status', 'status_changed']
        widgets = {'poll_type': forms.HiddenInput(),'create_user': forms.HiddenInput()}

    class Media:
        css = {
            'all': ('css/polls/poll_add.css',)
        }

class PollPurchaseForm(forms.ModelForm):

    class Meta:
        model = Poll
        exclude = ['status','status_changed', 'ranking_date']
        widgets = {'poll_type': forms.HiddenInput(),'create_user': forms.HiddenInput()}

    class Media:
        css = {
            'all': ('css/polls/poll_add.css',)
        }

class ItemsForm(forms.ModelForm):
    
    game = AutoCompleteSelectField('poll_game', required=True, plugin_options = {'autoFocus': True, 'minLength': 1})

    class Meta:
        model = Item
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Jogo já indicado por um associado.",
            }
        }
        widgets = {'poll': forms.HiddenInput(),'create_user': forms.HiddenInput()}

class AcceptsForm(forms.ModelForm):

    class Meta:
        model = PurchaseAccept
        fields = '__all__'
        widgets = {'poll': forms.HiddenInput(),'create_user': forms.HiddenInput()}