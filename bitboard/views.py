# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# importing loading from django template
from django.template import loader

def index(request):

    # getting the template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())
