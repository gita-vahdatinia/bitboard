# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Cryptocurrency
from .models import Cryptocompare
from .models import News
from .models import Profile

admin.site.register(Cryptocurrency)
admin.site.register(Cryptocompare)
admin.site.register(News)
admin.site.register(Profile)
