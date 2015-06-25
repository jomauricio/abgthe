# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

	def __unicode__(self):
		if self.first_name:
			return self.first_name
		else:
			return self.username