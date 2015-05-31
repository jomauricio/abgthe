# -*- coding: utf-8 -*-
#from django import forms
from ckeditor.widgets import CKEditorWidget
#from ajax_select import make_ajax_field
from apps.games.models import Game, Expansion
from django.conf import settings
from ajax_select.fields import AutoCompleteField
import floppyforms.__future__ as forms


class GamesForm(forms.ModelForm):
    
    description = forms.CharField(label="Descriçao", required=False, widget=CKEditorWidget())

    class Meta:
        model = Game
        fields = '__all__'

class ExpansionsForm(forms.ModelForm):
    
    description = forms.CharField(label="Descriçao", required=False, widget=CKEditorWidget())

    class Meta:
        model = Expansion
        fields = '__all__'

class SearchGamesForm(forms.Form):

    q = AutoCompleteField(
            'game',
            required=True,
            #help_text="Pesquise por jogos.",
            label="",
            show_help_text=False,
            attrs={'size': 50, 'placeholder':'Buscar por Jogos'}
            )

    class Media:
        css = {
            'all': ('css/games/game_list.css',)
        }
