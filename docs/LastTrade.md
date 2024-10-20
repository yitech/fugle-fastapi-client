# LastTrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid** | **float** |  | 
**ask** | **float** |  | 
**price** | **float** |  | 
**size** | **int** |  | 
**time** | **int** |  | 
**serial** | **int** |  | 

## Example

```python
from openapi_client.models.last_trade import LastTrade

# TODO update the JSON string below
json = "{}"
# create an instance of LastTrade from a JSON string
last_trade_instance = LastTrade.from_json(json)
# print the JSON string representation of the object
print(LastTrade.to_json())

# convert the object into a dict
last_trade_dict = last_trade_instance.to_dict()
# create an instance of LastTrade from a dict
last_trade_from_dict = LastTrade.from_dict(last_trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


