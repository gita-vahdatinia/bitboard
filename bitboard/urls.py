from django.conf.urls import url
from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /cryptocurrency/
    url(r'^cryptocurrency/$', views.cryptocurrency, name='cryptocurrency'),

    # /cryptocurrency/bitcoin/
    url(r'^(cryptocurrency/)(?P<token_tag>[A-Za-z0-9_-]+)/$', views.token, name='token'),

]
