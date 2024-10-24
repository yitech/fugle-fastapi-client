# fugle_fastapi_client.OrderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order_endpoint_api_v1_order_post**](OrderApi.md#create_order_endpoint_api_v1_order_post) | **POST** /api/v1/order | Create Order Endpoint
[**delete_order_endpoint_api_v1_order_ord_no_delete**](OrderApi.md#delete_order_endpoint_api_v1_order_ord_no_delete) | **DELETE** /api/v1/order/{ord_no} | Delete Order Endpoint
[**get_market_status_endpoint_api_v1_market_status_get**](OrderApi.md#get_market_status_endpoint_api_v1_market_status_get) | **GET** /api/v1/market_status | Get Market Status Endpoint
[**get_orders_endpoint_api_v1_orders_get**](OrderApi.md#get_orders_endpoint_api_v1_orders_get) | **GET** /api/v1/orders | Get Orders Endpoint


# **create_order_endpoint_api_v1_order_post**
> OrderResponse create_order_endpoint_api_v1_order_post(create_order)

Create Order Endpoint

### Example


```python
import fugle_fastapi_client
from fugle_fastapi_client.models.create_order import CreateOrder
from fugle_fastapi_client.models.order_response import OrderResponse
from fugle_fastapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fugle_fastapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fugle_fastapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugle_fastapi_client.OrderApi(api_client)
    create_order = fugle_fastapi_client.CreateOrder() # CreateOrder | 

    try:
        # Create Order Endpoint
        api_response = api_instance.create_order_endpoint_api_v1_order_post(create_order)
        print("The response of OrderApi->create_order_endpoint_api_v1_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_order_endpoint_api_v1_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order** | [**CreateOrder**](CreateOrder.md)|  | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_endpoint_api_v1_order_ord_no_delete**
> CancelResponse delete_order_endpoint_api_v1_order_ord_no_delete(ord_no)

Delete Order Endpoint

### Example


```python
import fugle_fastapi_client
from fugle_fastapi_client.models.cancel_response import CancelResponse
from fugle_fastapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fugle_fastapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fugle_fastapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugle_fastapi_client.OrderApi(api_client)
    ord_no = 'ord_no_example' # str | 

    try:
        # Delete Order Endpoint
        api_response = api_instance.delete_order_endpoint_api_v1_order_ord_no_delete(ord_no)
        print("The response of OrderApi->delete_order_endpoint_api_v1_order_ord_no_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->delete_order_endpoint_api_v1_order_ord_no_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ord_no** | **str**|  | 

### Return type

[**CancelResponse**](CancelResponse.md)

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

# **get_market_status_endpoint_api_v1_market_status_get**
> MarketStatusResponse get_market_status_endpoint_api_v1_market_status_get()

Get Market Status Endpoint

### Example


```python
import fugle_fastapi_client
from fugle_fastapi_client.models.market_status_response import MarketStatusResponse
from fugle_fastapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fugle_fastapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fugle_fastapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugle_fastapi_client.OrderApi(api_client)

    try:
        # Get Market Status Endpoint
        api_response = api_instance.get_market_status_endpoint_api_v1_market_status_get()
        print("The response of OrderApi->get_market_status_endpoint_api_v1_market_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_market_status_endpoint_api_v1_market_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MarketStatusResponse**](MarketStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_endpoint_api_v1_orders_get**
> List[OrderResultResponse] get_orders_endpoint_api_v1_orders_get()

Get Orders Endpoint

### Example


```python
import fugle_fastapi_client
from fugle_fastapi_client.models.order_result_response import OrderResultResponse
from fugle_fastapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fugle_fastapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fugle_fastapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugle_fastapi_client.OrderApi(api_client)

    try:
        # Get Orders Endpoint
        api_response = api_instance.get_orders_endpoint_api_v1_orders_get()
        print("The response of OrderApi->get_orders_endpoint_api_v1_orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_orders_endpoint_api_v1_orders_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrderResultResponse]**](OrderResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

