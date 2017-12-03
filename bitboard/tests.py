# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import News

class NewsModelTest(TestCase):
    def test_string_representation(self):
        news = News(title="7 Tokens Investors Are Talking About")
        news.save()
        self.assertEqual(str(news), news.title)
# Create your tests here.
