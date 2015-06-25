from django.db.models.signals import post_save
from django.dispatch import receiver
from abgthe.profiles.models import Profile
from abgthe.users.models import User
from allauth.socialaccount.models import SocialAccount
from allauth.account.signals import user_signed_up
from django.core.files import File
from avatar.models import Avatar
from urllib2 import urlopen
import requests
from django.core.files.temp import NamedTemporaryFile


def download_avatar(self, url):
	"""
	"""
	r = requests.get(url)

	img_temp = NamedTemporaryFile(delete=True)
	img_temp.write(r.content)
	img_temp.flush()
	img_temp.seek(0)
	return File(img_temp)

@receiver(post_save, sender=User)
def save_in_user(sender, **kwargs):
	obj=kwargs['instance']
	created=kwargs['created']
	if created:
		p = Profile(user=obj, username=obj.username)
		p.save()

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