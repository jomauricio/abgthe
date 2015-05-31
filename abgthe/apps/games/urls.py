# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from apps.games import views

urlpatterns = patterns('',
    url(r'^$',views.GameListView.as_view(),name='game_list'),
    url(r'^game/(?P<slug>[-_\w]+)/$',views.GameDetailView.as_view(),name='game_detail'),
    #url(r'^game/add/$', views.GameCreateView.as_view(), name='game_add'),
    #url(r'^game/(?P<slug>[-_\w]+)/update/$', views.GameUpdateView.as_view(), name='game_update'),
    #url(r'^game/(?P<slug>[-_\w]+)/delete/$', views.GameDeleteView.as_view(), name='game_delete'),

    url(r'^expansion/(?P<slug>[-_\w]+)/$',views.ExpansionDetailView.as_view(),name='expansion_detail'),
    #url(r'^expansion/add/$', views.ExpansionCreateView.as_view(), name='expansion_add'),
    #url(r'^expansion/(?P<slug>[-_\w]+)/update/$', views.ExpansionUpdateView.as_view(), name='expansion_update'),
    #url(r'^expansion/(?P<slug>[-_\w]+)/delete/$', views.ExpansionDeleteView.as_view(), name='expansion_delete'),

)
