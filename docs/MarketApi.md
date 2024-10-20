# openapi_client.MarketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_candles_api_v1_historical_candles_get**](MarketApi.md#get_candles_api_v1_historical_candles_get) | **GET** /api/v1/historical/candles | Get Candles
[**get_quote_api_v1_intraday_quote_get**](MarketApi.md#get_quote_api_v1_intraday_quote_get) | **GET** /api/v1/intraday/quote | Get Quote


# **get_candles_api_v1_historical_candles_get**
> KLines get_candles_api_v1_historical_candles_get(symbol, from_date, to_date, resolution=resolution)

Get Candles

### Example


```python
import openapi_client
from openapi_client.models.k_lines import KLines
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketApi(api_client)
    symbol = 'symbol_example' # str | 
    from_date = 'from_date_example' # str | 
    to_date = 'to_date_example' # str | 
    resolution = 'D' # str |  (optional) (default to 'D')

    try:
        # Get Candles
        api_response = api_instance.get_candles_api_v1_historical_candles_get(symbol, from_date, to_date, resolution=resolution)
        print("The response of MarketApi->get_candles_api_v1_historical_candles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_candles_api_v1_historical_candles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **from_date** | **str**|  | 
 **to_date** | **str**|  | 
 **resolution** | **str**|  | [optional] [default to &#39;D&#39;]

### Return type

[**KLines**](KLines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_api_v1_intraday_quote_get**
> Quote get_quote_api_v1_intraday_quote_get(symbol, type=type)

Get Quote

### Example


```python
import openapi_client
from openapi_client.models.quote import Quote
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketApi(api_client)
    symbol = 'symbol_example' # str | 
    type = EQUITY # str |  (optional) (default to EQUITY)

    try:
        # Get Quote
        api_response = api_instance.get_quote_api_v1_intraday_quote_get(symbol, type=type)
        print("The response of MarketApi->get_quote_api_v1_intraday_quote_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_quote_api_v1_intraday_quote_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **type** | **str**|  | [optional] [default to EQUITY]

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

