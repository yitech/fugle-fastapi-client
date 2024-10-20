# openapi_client.WalletApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance_endpoint_api_v1_balance_get**](WalletApi.md#get_balance_endpoint_api_v1_balance_get) | **GET** /api/v1/balance | Get Balance Endpoint
[**get_inventories_endpoint_api_v1_inventories_get**](WalletApi.md#get_inventories_endpoint_api_v1_inventories_get) | **GET** /api/v1/inventories | Get Inventories Endpoint
[**get_settlements_endpoint_api_v1_settlements_get**](WalletApi.md#get_settlements_endpoint_api_v1_settlements_get) | **GET** /api/v1/settlements | Get Settlements Endpoint


# **get_balance_endpoint_api_v1_balance_get**
> BalanceResponse get_balance_endpoint_api_v1_balance_get()

Get Balance Endpoint

### Example


```python
import openapi_client
from openapi_client.models.balance_response import BalanceResponse
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
    api_instance = openapi_client.WalletApi(api_client)

    try:
        # Get Balance Endpoint
        api_response = api_instance.get_balance_endpoint_api_v1_balance_get()
        print("The response of WalletApi->get_balance_endpoint_api_v1_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_balance_endpoint_api_v1_balance_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BalanceResponse**](BalanceResponse.md)

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

# **get_inventories_endpoint_api_v1_inventories_get**
> List[InventoryResponse] get_inventories_endpoint_api_v1_inventories_get()

Get Inventories Endpoint

### Example


```python
import openapi_client
from openapi_client.models.inventory_response import InventoryResponse
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
    api_instance = openapi_client.WalletApi(api_client)

    try:
        # Get Inventories Endpoint
        api_response = api_instance.get_inventories_endpoint_api_v1_inventories_get()
        print("The response of WalletApi->get_inventories_endpoint_api_v1_inventories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_inventories_endpoint_api_v1_inventories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[InventoryResponse]**](InventoryResponse.md)

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

# **get_settlements_endpoint_api_v1_settlements_get**
> List[SettlementResponse] get_settlements_endpoint_api_v1_settlements_get()

Get Settlements Endpoint

### Example


```python
import openapi_client
from openapi_client.models.settlement_response import SettlementResponse
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
    api_instance = openapi_client.WalletApi(api_client)

    try:
        # Get Settlements Endpoint
        api_response = api_instance.get_settlements_endpoint_api_v1_settlements_get()
        print("The response of WalletApi->get_settlements_endpoint_api_v1_settlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_settlements_endpoint_api_v1_settlements_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SettlementResponse]**](SettlementResponse.md)

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

