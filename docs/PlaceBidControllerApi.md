# openapi_client.PlaceBidControllerApi

All URIs are relative to *https://datsorange.devteam.games*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_best_price_buy_bid**](PlaceBidControllerApi.md#place_best_price_buy_bid) | **POST** /BestPriceBuy | Размещает заявку на покупку по &#39;лучшей цене&#39;
[**place_best_price_sell_bid**](PlaceBidControllerApi.md#place_best_price_sell_bid) | **POST** /BestPriceSell | Размещает заявку на продажу по &#39;лучшей цене&#39;
[**place_limit_price_buy_bid**](PlaceBidControllerApi.md#place_limit_price_buy_bid) | **POST** /LimitPriceBuy | Размещает заявку на покупку по цене не более установленной
[**place_limit_price_sell_bid**](PlaceBidControllerApi.md#place_limit_price_sell_bid) | **POST** /LimitPriceSell | Размещает заявку на продажу по цене не менее установленной
[**remove_bid**](PlaceBidControllerApi.md#remove_bid) | **POST** /RemoveBid | Отменяет заявку


# **place_best_price_buy_bid**
> list[BidResponse] place_best_price_buy_bid(token, best_price_bid_req)

Размещает заявку на покупку по 'лучшей цене'

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
    api_instance = openapi_client.PlaceBidControllerApi(api_client)
    token = 'token_example' # str | 
best_price_bid_req = openapi_client.BestPriceBidReq() # BestPriceBidReq | 

    try:
        # Размещает заявку на покупку по 'лучшей цене'
        api_response = api_instance.place_best_price_buy_bid(token, best_price_bid_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaceBidControllerApi->place_best_price_buy_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **best_price_bid_req** | [**BestPriceBidReq**](BestPriceBidReq.md)|  | 

### Return type

[**list[BidResponse]**](BidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_best_price_sell_bid**
> list[BidResponse] place_best_price_sell_bid(token, best_price_bid_req)

Размещает заявку на продажу по 'лучшей цене'

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
    api_instance = openapi_client.PlaceBidControllerApi(api_client)
    token = 'token_example' # str | 
best_price_bid_req = openapi_client.BestPriceBidReq() # BestPriceBidReq | 

    try:
        # Размещает заявку на продажу по 'лучшей цене'
        api_response = api_instance.place_best_price_sell_bid(token, best_price_bid_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaceBidControllerApi->place_best_price_sell_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **best_price_bid_req** | [**BestPriceBidReq**](BestPriceBidReq.md)|  | 

### Return type

[**list[BidResponse]**](BidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_limit_price_buy_bid**
> list[BidResponse] place_limit_price_buy_bid(token, limit_price_bid_req)

Размещает заявку на покупку по цене не более установленной

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
    api_instance = openapi_client.PlaceBidControllerApi(api_client)
    token = 'token_example' # str | 
limit_price_bid_req = openapi_client.LimitPriceBidReq() # LimitPriceBidReq | 

    try:
        # Размещает заявку на покупку по цене не более установленной
        api_response = api_instance.place_limit_price_buy_bid(token, limit_price_bid_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaceBidControllerApi->place_limit_price_buy_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **limit_price_bid_req** | [**LimitPriceBidReq**](LimitPriceBidReq.md)|  | 

### Return type

[**list[BidResponse]**](BidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_limit_price_sell_bid**
> list[BidResponse] place_limit_price_sell_bid(token, limit_price_bid_req)

Размещает заявку на продажу по цене не менее установленной

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
    api_instance = openapi_client.PlaceBidControllerApi(api_client)
    token = 'token_example' # str | 
limit_price_bid_req = openapi_client.LimitPriceBidReq() # LimitPriceBidReq | 

    try:
        # Размещает заявку на продажу по цене не менее установленной
        api_response = api_instance.place_limit_price_sell_bid(token, limit_price_bid_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaceBidControllerApi->place_limit_price_sell_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **limit_price_bid_req** | [**LimitPriceBidReq**](LimitPriceBidReq.md)|  | 

### Return type

[**list[BidResponse]**](BidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_bid**
> remove_bid(token, remove_bid_req)

Отменяет заявку

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
    api_instance = openapi_client.PlaceBidControllerApi(api_client)
    token = 'token_example' # str | 
remove_bid_req = openapi_client.RemoveBidReq() # RemoveBidReq | 

    try:
        # Отменяет заявку
        api_instance.remove_bid(token, remove_bid_req)
    except ApiException as e:
        print("Exception when calling PlaceBidControllerApi->remove_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **remove_bid_req** | [**RemoveBidReq**](RemoveBidReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

