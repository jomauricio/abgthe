# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from ajax_select import urls as ajax_select_urls

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^estatuto/$', TemplateView.as_view(template_name='pages/estatuto.html'), name="estatuto"),

    # Django Admin
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("abgthe.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),


    # Your stuff: custom urls includes go here
    url(r'^avatar/', include('avatar.urls')),
    url(r'^profile/', include('abgthe.profiles.urls', namespace='profiles')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]