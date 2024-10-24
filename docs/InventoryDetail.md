# InventoryDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy_sell** | **str** |  | 
**cost_r** | **float** |  | [optional] 
**fee** | **float** |  | 
**make_a** | **float** |  | 
**make_a_per** | **float** |  | 
**ord_no** | **str** |  | 
**pay_n** | **float** |  | 
**price** | **float** |  | 
**price_evn** | **float** |  | 
**qty** | **int** |  | 
**qty_c** | **int** |  | [optional] 
**qty_h** | **int** |  | [optional] 
**qty_r** | **int** |  | [optional] 
**t_date** | **str** |  | 
**t_time** | **str** |  | [optional] 
**tax** | **float** |  | [optional] 
**tax_g** | **float** |  | [optional] 
**trade** | **int** |  | [optional] 
**value_mkt** | **float** |  | 
**value_now** | **float** |  | 
**user_def** | **str** |  | [optional] 

## Example

```python
from fugle_fastapi_client.models.inventory_detail import InventoryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDetail from a JSON string
inventory_detail_instance = InventoryDetail.from_json(json)
# print the JSON string representation of the object
print(InventoryDetail.to_json())

# convert the object into a dict
inventory_detail_dict = inventory_detail_instance.to_dict()
# create an instance of InventoryDetail from a dict
inventory_detail_from_dict = InventoryDetail.from_dict(inventory_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


