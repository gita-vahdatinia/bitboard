# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitboard', '0013_auto_20171018_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocompare',
            name='sort_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cryptocompare',
            name='total_coin_supply',
            field=models.DecimalField(decimal_places=2, max_digits=200, null=True),
        ),
    ]