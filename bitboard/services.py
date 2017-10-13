import requests
import json
from coinmarketcap import Market

def get_tokens():
    url = 'https://api.coinmarketcap.com/v1/ticker/'
    r = requests.get(url)
    tokens = r.json()
    token_list = []
    for token in tokens:
        token_data = {'id': None, 'name': None, 'symbol': None, 'rank': None, 'price_usd': None, 'price_btc': None, '24h_volume_usd': None, 'market_cap_usd': None, 'available_supply': None, 'total_supply': None, 'percent_change_1h': None, 'percent_change_24h': None, 'percent_change_7d': None, 'last_updated': None }
        token_data['id'] = token['id']
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

def get_tokens_api():
    coinmarketcap = Market()
    return coinmarketcap

if __name__ == "__main__":
    tokens = get_tokens()
