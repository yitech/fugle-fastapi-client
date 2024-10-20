# OrderResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ap_code** | [**APCode**](APCode.md) |  | 
**avg_price** | **float** |  | 
**bs_flag** | [**BSFlag**](BSFlag.md) |  | 
**buy_sell** | [**Action**](Action.md) |  | 
**cel_qty** | **float** |  | 
**cel_qty_share** | **int** |  | 
**celable** | **str** |  | 
**err_code** | **str** |  | 
**err_msg** | **str** |  | 
**mat_qty** | **float** |  | 
**mat_qty_share** | **int** |  | 
**od_price** | **float** |  | 
**ord_date** | **str** |  | 
**ord_no** | **str** |  | 
**ord_status** | **str** |  | 
**ord_time** | **str** |  | 
**org_qty** | **float** |  | 
**org_qty_share** | **int** |  | 
**pre_ord_no** | **str** |  | 
**price_flag** | [**PriceFlag**](PriceFlag.md) |  | 
**stock_no** | **str** |  | 
**trade** | [**Trade**](Trade.md) |  | 
**work_date** | **str** |  | 
**user_def** | **str** |  | [optional] [default to '']

## Example

```python
from openapi_client.models.order_result_response import OrderResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResultResponse from a JSON string
order_result_response_instance = OrderResultResponse.from_json(json)
# print the JSON string representation of the object
print(OrderResultResponse.to_json())

# convert the object into a dict
order_result_response_dict = order_result_response_instance.to_dict()
# create an instance of OrderResultResponse from a dict
order_result_response_from_dict = OrderResultResponse.from_dict(order_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


