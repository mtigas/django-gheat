from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('gheat_demo.friends.views',
    # The basic HTML page that serves as our map view.
    url(
        regex   = r'^$',
        view    = direct_to_template, 
        name    = 'home',
        kwargs  = {
            'template': 'home.html',
            'extra_context': {
                'google_key':getattr(settings,'GOOGLE_API_KEY','')
                }
            }
    ),
    # URL pattern that serves tiles at the path that Google Maps API expects
    # ex.: /friends/tiles/fire/12/3,2.png
    url(
        regex = r'^tiles/(?P<color_scheme>\w+)/(?P<zoom>\d+)/(?P<x>\d+),(?P<y>\d+).png$',
        view = 'serve_tile',
        name = 'serve_tile',
    ),
)
