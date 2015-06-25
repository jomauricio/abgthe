# -*- coding: utf-8 -*-
#from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Profile
from django.conf import settings
from localflavor.br import forms as br_forms
import floppyforms.__future__ as forms
from django.conf import settings

class ProfilesForm(forms.ModelForm):

	description = forms.CharField(label="Descriçao",required=False, widget=CKEditorWidget())
	cep = br_forms.BRZipCodeField(label="CEP", required=False, widget=forms.TextInput(attrs={'placeholder': 'XXXXX-XXX'}))
	cel_phone = br_forms.BRPhoneNumberField(label="Celular", required=False, widget=forms.TextInput(attrs={'placeholder': 'XX-XXXX-XXXX'}))
	home_phone = br_forms.BRPhoneNumberField(label="Fixo", required=False, widget=forms.TextInput(attrs={'placeholder': 'XX-XXXX-XXXX'}))

	class Meta:
		model = Profile
		exclude  = ['user']

	class Media:
		css = {
			'all': ('css/profiles/profile_update.css',)
		}
