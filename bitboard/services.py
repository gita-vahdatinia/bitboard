import requests
import json
from coinmarketcap import Market
from .models import Cryptocurrency

def get_tokens_api():
    coinmarketcap = Market()
    return coinmarketcap

def get_tokens():
    url = 'https://api.coinmarketcap.com/v1/ticker/'
    r = requests.get(url)
    tokens = r.json()
    token_list = []
    for token in tokens:
        token_data = {'tag': None, 'name': None, 'symbol': None, 'rank': None, 'price_usd': None, 'price_btc': None, '24h_volume_usd': None, 'market_cap_usd': None, 'available_supply': None, 'total_supply': None, 'percent_change_1h': None, 'percent_change_24h': None, 'percent_change_7d': None, 'last_updated': None }
        token_data['tag'] = token['id']
        token_data['name'] = token['name']
        token_data['symbol'] = token['symbol']
        token_data['rank'] = token['rank']
        token_data['price_usd'] = token['price_usd']
        token_data['price_btc'] = token['price_btc']
        token_data['24h_volume_usd'] = token['24h_volume_usd']
        token_data['market_cap_usd'] = token['market_cap_usd']
        token_data['available_supply'] = token['available_supply']
        token_data['total_supply'] = token['total_supply']
        token_data['percent_change_1h'] = token['percent_change_1h']
        token_data['percent_change_24h'] = token['percent_change_24h']
        token_data['percent_change_7d'] = token['percent_change_7d']
        token_data['last_updated'] = token['last_updated']
        token_list.append(token_data)
    return token_list

def add_tokens_to_database():
    token_list = get_tokens()

    for token in token_list:

        token_tag = token['tag']
        token_name = token['name']
        token_symbol = token['symbol']
        token_rank = token['rank']
        token_price_usd = token['price_usd']
        token_price_btc = token['price_btc']
        token_24h_volume_usd = token['24h_volume_usd']
        token_market_cap_usd = token['market_cap_usd']
        token_available_supply = token['available_supply']
        token_total_supply = token['total_supply']
        token_percent_change_1h = token['percent_change_1h']
        token_percent_change_24h = token['percent_change_24h']
        token_percent_change_7d = token['percent_change_7d']
        token_last_updated = token['last_updated']

        if( not Cryptocurrency.objects.filter(tag=token_tag).exists() ):

            Cryptocurrency(
                            tag = token_tag,
                            name = token_name,
                            symbol = token_symbol,
                            rank = token_rank,
                            price_usd = token_price_usd,
                            price_btc = token_price_btc,
                            volume_24h_usd = token_24h_volume_usd,
                            market_cap_usd = token_market_cap_usd,
                            available_supply = token_available_supply,
                            total_supply = token_total_supply,
                            percent_change_1h = token_percent_change_1h,
                            percent_change_24h = token_percent_change_24h,
                            percent_change_7d = token_percent_change_7d,
                            last_updated = token_last_updated
                            ).save()
