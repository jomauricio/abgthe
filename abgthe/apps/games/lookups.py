from ajax_select import LookupChannel
from django.utils.html import escape
from django.db.models import Q
from .models import Game, Expansion
from django.core.urlresolvers import reverse

class GameLookup(LookupChannel):

    model = Game

    def get_query(self, q, request):
        return Game.objects.filter(name__icontains=q).order_by('name')

    def get_result(self, obj):
        u""" result is the simple text that is the completion of what the Game typed """
        return obj.name

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        url = reverse('games:game_detail', args=[obj.slug])
        url_img = '<img style='' src="http://placehold.it/80x90&amp;text=Sem imagem 40x80">'
        if obj.image:
            url_img = '<img style="margin-right: 5px;"" src="%s">' % obj.image.url

        return u"<div><a href='%s'>%s<i>%s</i></a></div>" % (url, url_img, escape(obj.name))

class ExpansionLookup(LookupChannel):

    model = Expansion

    def get_query(self, q, request):
        return Expansion.objects.filter(name__icontains=q).order_by('name')

    def get_result(self, obj):
        u""" result is the simple text that is the completion of what the Game typed """
        return obj.name

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        url = reverse('games:expansion_detail', args=[obj.slug])
        return u"<div><a href='%s'><i>%s</i></a></div>" % (url, escape(obj.name))