# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    # getting the template
    template = loader.get_template('bitboard/index.html')
    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def token(request, token_tag):
    return HttpResponse("You're looking at %s." % token_tag)
