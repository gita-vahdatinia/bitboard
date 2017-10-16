# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Cryptocurrency
from .services import add_tokens_to_database

def index(request):
    return render(request, 'bitboard/index.html')

def cryptocurrency(request):
    add_tokens_to_database()
    all_tokens = Cryptocurrency.objects.all()
    return render(request, 'bitboard/cryptocurrency.html', {"all_tokens": all_tokens})

def token(request, token_tag):
    try:
        token = Cryptocurrency.objects.get(tag=token_tag)
    except Cryptocurrency.DoesNotExist:
        raise Http404( token_tag + " does not exist")
    return render(request, 'bitboard/token.html', {"token": token})
