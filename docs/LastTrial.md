# LastTrial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid** | **float** |  | 
**ask** | **float** |  | 
**price** | **float** |  | 
**size** | **int** |  | 
**time** | **int** |  | 
**serial** | **int** |  | 

## Example

```python
from openapi_client.models.last_trial import LastTrial

# TODO update the JSON string below
json = "{}"
# create an instance of LastTrial from a JSON string
last_trial_instance = LastTrial.from_json(json)
# print the JSON string representation of the object
print(LastTrial.to_json())

# convert the object into a dict
last_trial_dict = last_trial_instance.to_dict()
# create an instance of LastTrial from a dict
last_trial_from_dict = LastTrial.from_dict(last_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


