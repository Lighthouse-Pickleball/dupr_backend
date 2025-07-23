# SingleWrapperPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PlayerResponse**](PlayerResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_player_response import SingleWrapperPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPlayerResponse from a JSON string
single_wrapper_player_response_instance = SingleWrapperPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPlayerResponse.to_json())

# convert the object into a dict
single_wrapper_player_response_dict = single_wrapper_player_response_instance.to_dict()
# create an instance of SingleWrapperPlayerResponse from a dict
single_wrapper_player_response_from_dict = SingleWrapperPlayerResponse.from_dict(single_wrapper_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


