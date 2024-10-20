# Total


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_value** | **int** |  | 
**trade_volume** | **int** |  | 
**trade_volume_at_bid** | **int** |  | 
**trade_volume_at_ask** | **int** |  | 
**transaction** | **int** |  | 
**time** | **int** |  | 

## Example

```python
from openapi_client.models.total import Total

# TODO update the JSON string below
json = "{}"
# create an instance of Total from a JSON string
total_instance = Total.from_json(json)
# print the JSON string representation of the object
print(Total.to_json())

# convert the object into a dict
total_dict = total_instance.to_dict()
# create an instance of Total from a dict
total_from_dict = Total.from_dict(total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


