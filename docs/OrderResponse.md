# OrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ord_date** | **str** |  | 
**ord_time** | **str** |  | 
**ord_type** | **str** |  | 
**ord_no** | **str** |  | 
**ret_code** | **str** |  | 
**ret_msg** | **str** |  | 
**work_date** | **str** |  | 

## Example

```python
from fugle_fastapi_client.models.order_response import OrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponse from a JSON string
order_response_instance = OrderResponse.from_json(json)
# print the JSON string representation of the object
print(OrderResponse.to_json())

# convert the object into a dict
order_response_dict = order_response_instance.to_dict()
# create an instance of OrderResponse from a dict
order_response_from_dict = OrderResponse.from_dict(order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


