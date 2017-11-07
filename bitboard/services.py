import requests
import json
import re
from .models import Cryptocurrency
from .models import Cryptocompare
from .models import News
import feedparser


# to remove the html tags on the description and titles of
# links provided in rss_to_database
TAG_RE = re.compile(r'<[^>]+>')
# characters to remove <p><sub><i>-- Delivered by <a href="http://feed43.com/">Feed43</a> service</i></sub></p>
def remove_tags(text):
    return TAG_RE.sub('', text)
# feeds to add to the table
def rss_to_database():
    rss_sources = {'recent':
        ['http://feeds.feedburner.com/CoinDesk',
        'http://bitcoin.worldnewsoffice.com/rss/category/1',
        'http://feed43.com/7570437205278443.xml'

        ],
        'popular':
        [
        ],
        'ethereum':
        ['http://feed43.com/7686530105373765.xml',
        ],
        'bitcoin':
        [
         'http://feed43.com/4124842572635051.xml'],
        'dogecoin':
        [
         'http://feed43.com/0788173065157115.xml'
        ]
        }
    tags = ['recent', 'popular', 'ethereum', 'bitcoin','dogecoin']
    for t in tags:
        for rss in rss_sources[t]:
            d = feedparser.parse(rss)

            for x in range(0, len(d['entries'])):
                if( not News.objects.filter(title=d.entries[x].title).exists()):
                    News(
                        tag = t,
                        title=(d.entries[x].title),
                        description=(d.entries[x].description),
                        link=d.entries[x].link
                        ).save()

            # print (d.namespaces)

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

        # update token
        else:

            token = Cryptocurrency.objects.get(tag=token_tag)
            token.rank = token_rank
            token.price_usd = token_price_usd
            token.price_btc = token_price_btc
            token.volume_24h_usd = token_24h_volume_usd
            token.market_cap_usd = token_market_cap_usd
            token.available_supply = token_available_supply
            token.total_supply = token_total_supply
            token.percent_change_1h = token_percent_change_1h
            token.percent_change_24h = token_percent_change_24h
            token.percent_change_7d = token_percent_change_7d
            token.last_updated = token_last_updated
            token.save()

def get_crypto_compare_coins():

    url = 'https://www.cryptocompare.com/api/data/coinlist/'
    r = requests.get(url)
    cryptocurrency = r.json()

    for index in cryptocurrency['Data']:

        coin = cryptocurrency['Data'][index]

        try:
            coin['ImageUrl'] = 'https://www.cryptocompare.com' + coin['ImageUrl']
        except:
            continue


        if( Cryptocurrency.objects.filter(symbol=coin['Symbol']).count() == 1 ):
            token = Cryptocurrency.objects.get(symbol=coin['Symbol'])
            token.image_url = coin['ImageUrl']
            token.save()


        # try:
        #     float(coin['TotalCoinSupply'])
        # except:
        #     coin['TotalCoinSupply'] = -1

        # url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + str(coin['Symbol']) + '&tsyms=BTC,USD'
        # r = requests.get(url)
        # price_data = r.json()

        # if( not Cryptocompare.objects.filter(coin_id=coin['Id']).exists() ):
        #
        #     Cryptocompare(
        #         coin_name=coin['CoinName'],
        #         name=coin['Name'],
        #         algorithm=coin['Algorithm'],
        #         url=coin['Url'],
        #         image_url=coin['ImageUrl'],
        #         coin_id=coin['Id'],
        #         proof_type=coin['ProofType'],
        #         sort_order=coin['SortOrder'],
        #         total_coin_supply=coin['TotalCoinSupply'],
        #         full_name=coin['FullName'],
        #         symbol=coin['Symbol'],
        #         # usd_change_24_hours=price_data['RAW'][str(coin['Symbol'])]['USD']['CHANGE24HOUR'],
        #         # percent_change_24_hours=price_data['RAW'][str(coin['Symbol'])]['USD']['CHANGEPCT24HOUR'],
        #         # supply=price_data['RAW'][str(coin['Symbol'])]['USD']['SUPPLY'],
        #         # market_cap_usd=price_data['RAW'][str(coin['Symbol'])]['USD']['MKTCAP']
        #
        #     ).save()
        #
        # else:
        #
        #     token = Cryptocompare.objects.get(coin['Id'])
        #     token.coin_name = coin['CoinName']
        #     token.name = coin['Name']
        #     token.algorithm = coin['Algorithm']
        #     token.url = coin['Url']
        #     token.image_url = coin['ImageUrl']
        #     token.coin_id = coin['Id']
        #     token.proof_type = coin['ProofType']
        #     token.sort_order = coin['SortOrder']
        #     token.total_coin_supply = coin['TotalCoinSupply']
        #     token.full_name = coin['FullName']
        #     token.symbol = coin['Symbol']
        #     token.save()
