from django.conf.urls import url
from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /news/
    url(r'^news/$', views.news, name='news'),

    # /profile/
    url(r'^profile/$', views.profile, name='profile'),

    # /cryptocurrency/
    url(r'^cryptocurrency/$', views.cryptocurrency, name='cryptocurrency'),

    # /cryptocurrency/bitcoin/
    url(r'^(cryptocurrency/)(?P<token_tag>[A-Za-z0-9_-]+)/$', views.token, name='token'),

]
