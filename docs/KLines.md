# KLines


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**type** | **str** |  | 
**exchange** | **str** |  | 
**market** | **str** |  | 
**timeframe** | **str** |  | 
**data** | [**List[KLine]**](KLine.md) |  | 

## Example

```python
from openapi_client.models.k_lines import KLines

# TODO update the JSON string below
json = "{}"
# create an instance of KLines from a JSON string
k_lines_instance = KLines.from_json(json)
# print the JSON string representation of the object
print(KLines.to_json())

# convert the object into a dict
k_lines_dict = k_lines_instance.to_dict()
# create an instance of KLines from a dict
k_lines_from_dict = KLines.from_dict(k_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


