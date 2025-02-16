# SingleWrapperOfPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PlayerResponse**](PlayerResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_player_response import SingleWrapperOfPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPlayerResponse from a JSON string
single_wrapper_of_player_response_instance = SingleWrapperOfPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPlayerResponse.to_json())

# convert the object into a dict
single_wrapper_of_player_response_dict = single_wrapper_of_player_response_instance.to_dict()
# create an instance of SingleWrapperOfPlayerResponse from a dict
single_wrapper_of_player_response_from_dict = SingleWrapperOfPlayerResponse.from_dict(single_wrapper_of_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


