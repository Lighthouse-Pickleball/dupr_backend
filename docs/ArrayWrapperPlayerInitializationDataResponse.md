# ArrayWrapperPlayerInitializationDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[PlayerInitializationDataResponse]**](PlayerInitializationDataResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_player_initialization_data_response import ArrayWrapperPlayerInitializationDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperPlayerInitializationDataResponse from a JSON string
array_wrapper_player_initialization_data_response_instance = ArrayWrapperPlayerInitializationDataResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperPlayerInitializationDataResponse.to_json())

# convert the object into a dict
array_wrapper_player_initialization_data_response_dict = array_wrapper_player_initialization_data_response_instance.to_dict()
# create an instance of ArrayWrapperPlayerInitializationDataResponse from a dict
array_wrapper_player_initialization_data_response_from_dict = ArrayWrapperPlayerInitializationDataResponse.from_dict(array_wrapper_player_initialization_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


