# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitboard', '0010_auto_20171018_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocompare',
            name='total_coin_supply',
            field=models.CharField(max_length=200, null=True),
        ),
    ]