# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from apps.profiles.views import ProfileUpdateView, ProfileDetailView, ProfileRedirectView

urlpatterns = patterns('',
	url(r'^redirect/$',ProfileRedirectView.as_view(),name='redirect'),
	url(r'^(?P<username>[\w.@+-]+)/$', ProfileDetailView.as_view(), name='profile_detail'),
	url(r'^(?P<username>[\w.@+-]+)/update/$', ProfileUpdateView.as_view(), name='profile_update'),
)