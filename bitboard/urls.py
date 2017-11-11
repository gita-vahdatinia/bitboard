from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /cryptocurrency/
    url(r'^news/$', views.news, name='news'),


    # /cryptocurrency/
    url(r'^cryptocurrency/$', views.cryptocurrency, name='cryptocurrency'),

    # /cryptocurrency/bitcoin/
    url(r'^(cryptocurrency/)(?P<token_tag>[A-Za-z0-9_-]+)/$', views.token, name='token'),

    # login stuff
    url(r'^login/$', auth_views.login, name='login'),

    url(r'^logout/$', auth_views.logout, name='logout'),

]
