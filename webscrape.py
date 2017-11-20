# import libraries
import urrlib2
from bs4 import BeautifulSoup

eth_url = 'https://www.ethnews.com/'
eth_page = urllib2.urlopen(eth_url)
eth_soup = BeautifulSoup(eth_page, 'html.parser')
