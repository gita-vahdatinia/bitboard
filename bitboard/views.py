# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Cryptocurrency
from .models import Cryptocompare
from .models import News
from .services import add_tokens_to_database
from .services import get_crypto_compare_coins
from .services import rss_to_database

# /
def index(request):
    return render(request, 'bitboard/index.html')

# /news
def news(request):
    rss_to_database()
    all_news_feeds = News.objects.all()
    return render(request, 'bitboard/news.html', {"all_news_feeds": all_news_feeds})

# /cryptocurrency
def cryptocurrency(request):
    #add_tokens_to_database()
#    get_crypto_compare_coins()
    all_tokens = Cryptocurrency.objects.all().order_by('rank')
    return render(request, 'bitboard/cryptocurrency.html', {"all_tokens": all_tokens})

# /cryptocurrency/bitcoin
def token(request, token_tag):
    try:
        token = Cryptocurrency.objects.get(tag=token_tag)
    except Cryptocurrency.DoesNotExist:
        raise Http404( token_tag + " does not exist")
    return render(request, 'bitboard/token.html', {"token": token})
