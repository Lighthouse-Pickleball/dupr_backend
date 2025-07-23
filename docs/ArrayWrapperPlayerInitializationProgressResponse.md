# ArrayWrapperPlayerInitializationProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[PlayerInitializationProgressResponse]**](PlayerInitializationProgressResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_player_initialization_progress_response import ArrayWrapperPlayerInitializationProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperPlayerInitializationProgressResponse from a JSON string
array_wrapper_player_initialization_progress_response_instance = ArrayWrapperPlayerInitializationProgressResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperPlayerInitializationProgressResponse.to_json())

# convert the object into a dict
array_wrapper_player_initialization_progress_response_dict = array_wrapper_player_initialization_progress_response_instance.to_dict()
# create an instance of ArrayWrapperPlayerInitializationProgressResponse from a dict
array_wrapper_player_initialization_progress_response_from_dict = ArrayWrapperPlayerInitializationProgressResponse.from_dict(array_wrapper_player_initialization_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


