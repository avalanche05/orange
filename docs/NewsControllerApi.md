# openapi_client.NewsControllerApi

All URIs are relative to *https://datsorange.devteam.games*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_news**](NewsControllerApi.md#get_latest_news) | **GET** /news/LatestNews | Возвращает последнюю новость
[**get_latest_news1**](NewsControllerApi.md#get_latest_news1) | **GET** /news/LatestNews1Minute | Возвращает новости за последнюю минуту
[**get_latest_news5**](NewsControllerApi.md#get_latest_news5) | **GET** /news/LatestNews5Minutes | Возвращает новости за последние 5 минут


# **get_latest_news**
> NewsResponse get_latest_news(token)

Возвращает последнюю новость

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
    api_instance = openapi_client.NewsControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        # Возвращает последнюю новость
        api_response = api_instance.get_latest_news(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NewsControllerApi->get_latest_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**NewsResponse**](NewsResponse.md)

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

# **get_latest_news1**
> list[NewsResponse] get_latest_news1(token)

Возвращает новости за последнюю минуту

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
    api_instance = openapi_client.NewsControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        # Возвращает новости за последнюю минуту
        api_response = api_instance.get_latest_news1(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NewsControllerApi->get_latest_news1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**list[NewsResponse]**](NewsResponse.md)

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

# **get_latest_news5**
> list[NewsResponse] get_latest_news5(token)

Возвращает новости за последние 5 минут

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
    api_instance = openapi_client.NewsControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        # Возвращает новости за последние 5 минут
        api_response = api_instance.get_latest_news5(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NewsControllerApi->get_latest_news5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**list[NewsResponse]**](NewsResponse.md)

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

