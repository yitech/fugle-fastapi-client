# QuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**type** | **str** |  | 
**exchange** | **str** |  | 
**market** | **str** |  | 
**symbol** | **str** |  | 
**name** | **str** |  | 
**reference_price** | **float** |  | 
**previous_close** | **float** |  | 
**open_price** | **float** |  | 
**open_time** | **int** |  | 
**high_price** | **float** |  | 
**high_time** | **int** |  | 
**low_price** | **float** |  | 
**low_time** | **int** |  | 
**close_price** | **float** |  | 
**close_time** | **int** |  | 
**avg_price** | **float** |  | 
**change** | **float** |  | 
**change_percent** | **float** |  | 
**amplitude** | **float** |  | 
**last_price** | **float** |  | 
**last_size** | **int** |  | 
**bids** | [**List[BidAsk]**](BidAsk.md) |  | 
**asks** | [**List[BidAsk]**](BidAsk.md) |  | 
**total** | [**Total**](Total.md) |  | 
**last_trade** | [**LastTrade**](LastTrade.md) |  | 
**last_trial** | [**LastTrial**](LastTrial.md) |  | 
**is_trial** | **bool** |  | [optional] 
**is_delayed_open** | **bool** |  | [optional] 
**is_delayed_close** | **bool** |  | [optional] 
**is_open** | **bool** |  | [optional] 
**is_close** | **bool** |  | [optional] 
**last_updated** | **int** |  | 
**serial** | **int** |  | 

## Example

```python
from fugle_fastapi_client.models.quote_response import QuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponse from a JSON string
quote_response_instance = QuoteResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteResponse.to_json())

# convert the object into a dict
quote_response_dict = quote_response_instance.to_dict()
# create an instance of QuoteResponse from a dict
quote_response_from_dict = QuoteResponse.from_dict(quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


