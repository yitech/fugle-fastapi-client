# KLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**open** | **float** |  | 
**high** | **float** |  | 
**low** | **float** |  | 
**close** | **float** |  | 
**volume** | **int** |  | 

## Example

```python
from openapi_client.models.k_line import KLine

# TODO update the JSON string below
json = "{}"
# create an instance of KLine from a JSON string
k_line_instance = KLine.from_json(json)
# print the JSON string representation of the object
print(KLine.to_json())

# convert the object into a dict
k_line_dict = k_line_instance.to_dict()
# create an instance of KLine from a dict
k_line_from_dict = KLine.from_dict(k_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


