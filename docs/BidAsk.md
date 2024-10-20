# BidAsk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | 
**size** | **int** |  | 

## Example

```python
from openapi_client.models.bid_ask import BidAsk

# TODO update the JSON string below
json = "{}"
# create an instance of BidAsk from a JSON string
bid_ask_instance = BidAsk.from_json(json)
# print the JSON string representation of the object
print(BidAsk.to_json())

# convert the object into a dict
bid_ask_dict = bid_ask_instance.to_dict()
# create an instance of BidAsk from a dict
bid_ask_from_dict = BidAsk.from_dict(bid_ask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


