# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from apps.polls import views

urlpatterns = patterns('',
    url(r'^$',views.PollListView.as_view(),name='poll_list'),
    url(r'^poll/sixlist/add/$',views.PollSixListCreateView.as_view(),name='poll_sixlist_add'),
    url(r'^poll/(?P<pk>\d+)/detail/$',views.PollSixListDetailView.as_view(),name='poll_sixlist_detail'),
    url(r'^poll/(?P<poll_pk>\d+)/item/add/$', views.ItemSixListCreateView.as_view(), name='sixlist_item_add'),
	url(r'^poll/(?P<poll_pk>\d+)/item/(?P<pk>\d+)/update/$',views.ItemSixListUpdateView.as_view(),name='sixlist_item_update'),
    url(r'^poll/(?P<poll_pk>\d+)/item/(?P<pk>\d+)/delete/$',views.ItemSixListDeleteView.as_view(),name='sixlist_item_delete'),
    url(r'^poll/(?P<poll_pk>\d+)/item/list/$',views.ItemListView.as_view(),name='poll_items_list'),
    url(r'^poll/(?P<poll_pk>\d+)/item/list/ranking$', views.SixListRankingView.as_view(), name='poll_item_ranking'),
    url(r'^poll/purchase/add/$',views.PollPurchaseCreateView.as_view(),name='poll_purchase_add'),
    url(r'^poll/(?P<pk>\d+)/purchase/$', views.PollPurchaseDetailView.as_view(), name='poll_purchase_detail'),
    url(r'^poll/(?P<poll_pk>\d+)/vote/add/$', views.PurchaseAcceptCreateView.as_view(), name='purchase_accept_add'),
    url(r'^poll/(?P<poll_pk>\d+)/vote/(?P<pk>\d+)/update/$',views.PurchaseAcceptUpdateView.as_view(),name='purchase_accept_update'),
    url(r'^poll/(?P<poll_pk>\d+)/vote/(?P<pk>\d+)/delete/$',views.PurchaseAcceptDeleteView.as_view(),name='purchase_accept_delete'),
)
