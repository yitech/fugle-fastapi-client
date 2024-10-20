# CreateOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy_sell** | [**Action**](Action.md) |  | 
**ap_code** | [**APCode**](APCode.md) |  | 
**price_flag** | [**PriceFlag**](PriceFlag.md) |  | 
**bs_flag** | [**BSFlag**](BSFlag.md) |  | 
**trade** | [**Trade**](Trade.md) |  | 
**stock_no** | **str** |  | 
**quantity** | **int** |  | 
**price** | **float** |  | 

## Example

```python
from openapi_client.models.create_order import CreateOrder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrder from a JSON string
create_order_instance = CreateOrder.from_json(json)
# print the JSON string representation of the object
print(CreateOrder.to_json())

# convert the object into a dict
create_order_dict = create_order_instance.to_dict()
# create an instance of CreateOrder from a dict
create_order_from_dict = CreateOrder.from_dict(create_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


