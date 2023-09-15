# openapi_client.InfoControllerApi

All URIs are relative to *https://datsorange.devteam.games*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_info**](InfoControllerApi.md#account_info) | **GET** /info | Информация о счете


# **account_info**
> InfoResponse account_info(token)

Информация о счете

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
    api_instance = openapi_client.InfoControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        # Информация о счете
        api_response = api_instance.account_info(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InfoControllerApi->account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**InfoResponse**](InfoResponse.md)

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

