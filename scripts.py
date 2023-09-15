# Import the generated client
from openapi_client import Configuration
from openapi_client.api.news_controller_api import NewsControllerApi
from openapi_client.api.stock_info_api import StockInfoApi
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

r = stock.getsymbols(token)


def get_symbol_id_by_name(symbol_name):
    symbols = stock.getsymbols(token)

    for symbol in symbols:
        if symbol.ticker == symbol_name:
            return symbol.id




print(get_symbol_id_by_name('Oranges/TreeSavvy Forestry'))
