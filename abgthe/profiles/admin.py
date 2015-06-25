from django.contrib import admin
from .models import Profile
from .forms import ProfilesForm
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	form = ProfilesForm