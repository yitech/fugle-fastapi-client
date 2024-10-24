# KLinesResponse


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
from fugle_fastapi_client.models.k_lines_response import KLinesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KLinesResponse from a JSON string
k_lines_response_instance = KLinesResponse.from_json(json)
# print the JSON string representation of the object
print(KLinesResponse.to_json())

# convert the object into a dict
k_lines_response_dict = k_lines_response_instance.to_dict()
# create an instance of KLinesResponse from a dict
k_lines_response_from_dict = KLinesResponse.from_dict(k_lines_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


