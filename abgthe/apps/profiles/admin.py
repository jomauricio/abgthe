from django.contrib import admin
from jmauricio.apps.profiles.models import Profile
from jmauricio.apps.profiles.forms import ProfilesForm
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	form = ProfilesForm