# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin\

# Register your models here.

from .models import Cryptocurrency
from .models import Cryptocompare

admin.site.register(Cryptocurrency)
admin.site.register(Cryptocompare)
