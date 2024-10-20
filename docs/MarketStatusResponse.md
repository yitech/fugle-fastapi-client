# MarketStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_trading_day** | **bool** |  | 
**last_trading_day** | **str** |  | 
**next_trading_day** | **str** |  | 

## Example

```python
from openapi_client.models.market_status_response import MarketStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketStatusResponse from a JSON string
market_status_response_instance = MarketStatusResponse.from_json(json)
# print the JSON string representation of the object
print(MarketStatusResponse.to_json())

# convert the object into a dict
market_status_response_dict = market_status_response_instance.to_dict()
# create an instance of MarketStatusResponse from a dict
market_status_response_from_dict = MarketStatusResponse.from_dict(market_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


