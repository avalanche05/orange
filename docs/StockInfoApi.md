# openapi_client.StockInfoApi

All URIs are relative to *https://datsorange.devteam.games*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buy_stock_by_symbol_id**](StockInfoApi.md#get_buy_stock_by_symbol_id) | **GET** /buyStock | Заявки на покупку
[**get_sell_stock_by_symbol_id**](StockInfoApi.md#get_sell_stock_by_symbol_id) | **GET** /sellStock | Заявки на продажу
[**getsymbols**](StockInfoApi.md#getsymbols) | **GET** /getSymbols | Список всех активов


# **get_buy_stock_by_symbol_id**
> list[StockResp] get_buy_stock_by_symbol_id(token)

Заявки на покупку

Возвращает количество активных заявок и их цену

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://datsorange.devteam.games
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://datsorange.devteam.games"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StockInfoApi(api_client)
    token = 'token' # str | Токен доступа

    try:
        # Заявки на покупку
        api_response = api_instance.get_buy_stock_by_symbol_id(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockInfoApi->get_buy_stock_by_symbol_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Токен доступа | 

### Return type

[**list[StockResp]**](StockResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sell_stock_by_symbol_id**
> list[StockResp] get_sell_stock_by_symbol_id(token)

Заявки на продажу

Возвращает количество активных заявок и их цену

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://datsorange.devteam.games
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://datsorange.devteam.games"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StockInfoApi(api_client)
    token = 'token' # str | Токен доступа

    try:
        # Заявки на продажу
        api_response = api_instance.get_sell_stock_by_symbol_id(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockInfoApi->get_sell_stock_by_symbol_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Токен доступа | 

### Return type

[**list[StockResp]**](StockResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getsymbols**
> list[SymbolsResp] getsymbols(token)

Список всех активов

Возвращает список всех возможных активов

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://datsorange.devteam.games
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://datsorange.devteam.games"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StockInfoApi(api_client)
    token = 'token' # str | Токен доступа

    try:
        # Список всех активов
        api_response = api_instance.getsymbols(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockInfoApi->getsymbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Токен доступа | 

### Return type

[**list[SymbolsResp]**](SymbolsResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

