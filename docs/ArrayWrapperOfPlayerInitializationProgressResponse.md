# ArrayWrapperOfPlayerInitializationProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[PlayerInitializationProgressResponse]**](PlayerInitializationProgressResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_player_initialization_progress_response import ArrayWrapperOfPlayerInitializationProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfPlayerInitializationProgressResponse from a JSON string
array_wrapper_of_player_initialization_progress_response_instance = ArrayWrapperOfPlayerInitializationProgressResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfPlayerInitializationProgressResponse.to_json())

# convert the object into a dict
array_wrapper_of_player_initialization_progress_response_dict = array_wrapper_of_player_initialization_progress_response_instance.to_dict()
# create an instance of ArrayWrapperOfPlayerInitializationProgressResponse from a dict
array_wrapper_of_player_initialization_progress_response_from_dict = ArrayWrapperOfPlayerInitializationProgressResponse.from_dict(array_wrapper_of_player_initialization_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


