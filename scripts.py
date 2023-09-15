# Import the generated client
from openapi_client import Configuration
from openapi_client.api.news_controller_api import NewsControllerApi
from openapi_client.api.stock_info_api import StockInfoApi
from openapi_client.api.place_bid_controller_api import PlaceBidControllerApi
from openapi_client.models import *
from openapi_client.api_client import ApiClient

# Configure your base URL and token
base_url = "https://datsorange.devteam.games"
token = "64f433d6143b064f433d6143b3"

config = Configuration(host=base_url)
client = ApiClient(configuration=config,
                   header_name="token",
                   header_value=token)

news = NewsControllerApi(api_client=client)
stock = StockInfoApi(api_client=client)
bid = PlaceBidControllerApi(api_client=client)

r = stock.getsymbols(token)


def get_symbol_id_by_name(symbol_name):
    symbols = stock.getsymbols(token)

    for symbol in symbols:
        if symbol.ticker == symbol_name:
            return symbol.id


def stock_price(stock_name: str):
    res = stock.get_sell_stock_by_symbol_id(token)
    pass


import requests
import json
import time
from collections import defaultdict

session = requests.session()
session.headers.update(token="64f433d6143b064f433d6143b3")

companies = defaultdict(int)
last_news = ''

stock_price("wjfekjh")


idd = get_symbol_id_by_name("Oranges/TreeSavvy Forestry")
r = bid.place_limit_price_buy_bid(
    token,
    {
        "symbolId": int(idd),
        "price": 160,
        "quantity": 10
    }
)

pass

while True:
    pass


while True:
    LatestNews = session.get(
        url="https://datsorange.devteam.games/news/LatestNews"
    )
    data = LatestNews.json()
    if str(data['date']) != last_news:
        for company in data['companiesAffected']:
            companies[company] += data['rate']
        last_news = str(data['date'])
    time.sleep(30)
    max_company = min(companies.items(), key=lambda x: x[1])[0]
    print(max_company)
