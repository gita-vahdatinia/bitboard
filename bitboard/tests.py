# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.test import TestCase

from .models import News
from .models import Profile
from .models import Cryptocurrency



# test user model
# checks with database for proper storage of data
class NewsModelTest(TestCase):
    def test_string_representation(self):
        tg = "7 tokens"
        tl = "7 Tokens Investors Are Talking About"
        ds = "This is about 7 tokens"
        lk = "http://fakelink"
        news = News(tag=tg, title=tl, description=ds, link=lk)
        news.save()
        self.assertEqual(tg, news.tag)
        self.assertEqual(tl, news.title)
        self.assertEqual(ds, news.description)
        self.assertEqual(lk, news.link)

# test cryptocurrency model
# checks with database for proper storage of data
class CryptocurrencyTest(TestCase):
    def test_cryptocurrency_representation(self):
        tg = "bitcoin"
        nm = "Bitcoin"
        symb = "BTC"
        rk = 1
        prc_usd = 11000
        prc_btc = 1
        vol_24h_usd = 20000000
        mrk_cap_usd = 200000000000
        avl_supl = 16000000
        tot_sup = 21000000
        prc_cng_1h = 4
        prc_cng_24h = 42
        prc_cng_7d = 122
        coin = Cryptocurrency(
            tag=tg,
            name=nm,
            symbol=symb,
            rank=rk,
            price_usd=prc_usd,
            price_btc=prc_btc,
            volume_24h_usd=vol_24h_usd,
            market_cap_usd=mrk_cap_usd,
            available_supply=avl_supl,
            total_supply=tot_sup,
            percent_change_1h=prc_cng_1h,
            percent_change_24h=prc_cng_24h,
            percent_change_7d=prc_cng_7d
        )
        coin.save()
        self.assertEqual(tg, coin.tag)
        self.assertEqual(nm, coin.name)
        self.assertEqual(symb, coin.symbol)
        self.assertEqual(rk, coin.rank)
        self.assertEqual(prc_usd, coin.price_usd)
        self.assertEqual(prc_btc, coin.price_btc)
        self.assertEqual(vol_24h_usd, coin.volume_24h_usd)
        self.assertEqual(mrk_cap_usd, coin.market_cap_usd)
        self.assertEqual(avl_supl, coin.available_supply)
        self.assertEqual(tot_sup, coin.total_supply)
        self.assertEqual(prc_cng_1h, coin.percent_change_1h)
        self.assertEqual(prc_cng_24h, coin.percent_change_24h)
        self.assertEqual(prc_cng_7d, coin.percent_change_7d)

# test profile model
# checks with database for proper storage of data
class ProfileTest(TestCase):
    def test_profile_representation(self):
            bio = "Barrack Obama"
            loc = "Washington DC"
            brth_dt = "04/20/2140"
            user_profile = Profile(
                bio=bio,
                location=loc,
                birth_date=brth_dt
            )
            user_profile.save
            self.assertEqual(bio, user_profile.bio)
            self.assertEqual(loc, user_profile.location)
            self.assertEqual(brth_dt, user_profile.birth_date)
