# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
#from django.views.generic import CreateView
#from django.views.generic import UpdateView
#from django.views.generic import DeleteView
#from django.views.generic import RedirectView
from braces.views import LoginRequiredMixin
from .forms import GamesForm, SearchGamesForm, ExpansionsForm
from .models import Game, Expansion

from django.shortcuts import render_to_response
from django.template import RequestContext


class GameListView(LoginRequiredMixin, ListView):
    model = Game
    # These next two lines tell the view to index lookups by username
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GameListView, self).get_context_data(**kwargs)
        context['form'] = SearchGamesForm()
        return context

class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    slug_field = "slug"
    slug_url_kwarg = "slug"

class ExpansionDetailView(LoginRequiredMixin, DetailView):
    model = Expansion
    slug_field = "slug"
    slug_url_kwarg = "slug"