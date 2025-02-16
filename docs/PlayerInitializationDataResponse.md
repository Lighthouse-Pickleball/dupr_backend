# PlayerInitializationDataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_left_for_initialization** | **int** |  | [optional] 
**event_format** | **str** |  | 
**initialization_status** | **str** |  | 
**player_id** | **str** |  | 
**player_name** | **str** |  | 
**qualification_score** | **float** |  | 

## Example

```python
from dupr_backend.models.player_initialization_data_response import PlayerInitializationDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerInitializationDataResponse from a JSON string
player_initialization_data_response_instance = PlayerInitializationDataResponse.from_json(json)
# print the JSON string representation of the object
print PlayerInitializationDataResponse.to_json()

# convert the object into a dict
player_initialization_data_response_dict = player_initialization_data_response_instance.to_dict()
# create an instance of PlayerInitializationDataResponse from a dict
player_initialization_data_response_form_dict = player_initialization_data_response.from_dict(player_initialization_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


