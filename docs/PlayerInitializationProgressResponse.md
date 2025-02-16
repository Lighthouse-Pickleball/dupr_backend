# PlayerInitializationProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayerInitializationDataResponse**](PlayerInitializationDataResponse.md) |  | [optional] 
**message** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from dupr_backend.models.player_initialization_progress_response import PlayerInitializationProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerInitializationProgressResponse from a JSON string
player_initialization_progress_response_instance = PlayerInitializationProgressResponse.from_json(json)
# print the JSON string representation of the object
print PlayerInitializationProgressResponse.to_json()

# convert the object into a dict
player_initialization_progress_response_dict = player_initialization_progress_response_instance.to_dict()
# create an instance of PlayerInitializationProgressResponse from a dict
player_initialization_progress_response_form_dict = player_initialization_progress_response.from_dict(player_initialization_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


