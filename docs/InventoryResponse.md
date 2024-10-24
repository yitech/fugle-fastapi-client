# InventoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ap_code** | **str** |  | [optional] 
**cost_qty** | **float** |  | 
**cost_sum** | **float** |  | 
**make_a_per** | **float** |  | 
**make_a_sum** | **float** |  | 
**price_avg** | **float** |  | 
**price_evn** | **float** |  | 
**price_mkt** | **float** |  | 
**price_now** | **float** |  | 
**price_qty_sum** | **float** |  | 
**qty_b** | **int** |  | 
**qty_bm** | **int** |  | 
**qty_c** | **int** |  | 
**qty_l** | **int** |  | 
**qty_s** | **int** |  | 
**qty_sm** | **int** |  | 
**rec_va_sum** | **float** |  | 
**s_type** | **str** |  | 
**stk_dats** | [**List[InventoryDetail]**](InventoryDetail.md) |  | 
**stk_na** | **str** |  | 
**stk_no** | **str** |  | 
**trade** | **int** |  | [optional] 
**value_mkt** | **float** |  | 
**value_now** | **float** |  | 

## Example

```python
from fugle_fastapi_client.models.inventory_response import InventoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryResponse from a JSON string
inventory_response_instance = InventoryResponse.from_json(json)
# print the JSON string representation of the object
print(InventoryResponse.to_json())

# convert the object into a dict
inventory_response_dict = inventory_response_instance.to_dict()
# create an instance of InventoryResponse from a dict
inventory_response_from_dict = InventoryResponse.from_dict(inventory_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


