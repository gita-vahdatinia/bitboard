# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.test import TestCase

from .models import News
from .models import Profile


class NewsModelTest(TestCase):
    def test_string_representation(self):
        news = News(title="7 Tokens Investors Are Talking About")
        news.save()
        self.assertEqual(str(news), news.title)



# class ProfileModelTest(TestCase):
#     def test_name(self):
#         name = Profile(user="TestGuyPerson")
#         name.save()
#         self.assertEqual(str(name), name.user)
#     def test_bio(self):
#         bio = Profile(bio="I'm a cool guy")
#         bio.save()
#         self.assertEqual(str(bio), bio.bio)
#     def test_location(self):
#         location = Profile(location="Los Angeles")
#         location.assertEqual(str(location), location.location)
#     def test_birth(self):
#         birth = Profile(birth_date="November 6")
#         birth.save()
#         self.assertEqual(str(birth), birth.birth_date)
# Create your tests here.
