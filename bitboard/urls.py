from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from bitboard import views as bit_views




urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /cryptocurrency/
    url(r'^news/$', views.news, name='news'),


    # /cryptocurrency/
    url(r'^cryptocurrency/$', views.cryptocurrency, name='cryptocurrency'),

    # /cryptocurrency/bitcoin/
    url(r'^(cryptocurrency/)(?P<token_tag>[A-Za-z0-9_-]+)/$', views.token, name='token'),

    # /login
    url(r'^login/$', auth_views.login, name='login'),

    # /logout
    url(r'^logout/$', auth_views.logout, name='logout'),

    # /signup
    url(r'^signup/$', bit_views.signup, name='signup'),
]
