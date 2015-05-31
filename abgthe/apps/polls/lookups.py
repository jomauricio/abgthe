from ajax_select import LookupChannel
from django.utils.html import escape
from apps.games.lookups import GameLookup

class PollGameLookup(GameLookup):

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        url_img = '<img style='' src="http://placehold.it/80x90&amp;text=Sem imagem 40x80">'
        if obj.image:
            url_img = '<img style="margin-right: 5px;"" src="%s">' % obj.image.url

        return u"<div>%s<i>%s</i></div>" % (url_img, escape(obj.name))