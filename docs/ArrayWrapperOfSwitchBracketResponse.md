# ArrayWrapperOfSwitchBracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[SwitchBracketResponse]**](SwitchBracketResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_switch_bracket_response import ArrayWrapperOfSwitchBracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfSwitchBracketResponse from a JSON string
array_wrapper_of_switch_bracket_response_instance = ArrayWrapperOfSwitchBracketResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfSwitchBracketResponse.to_json())

# convert the object into a dict
array_wrapper_of_switch_bracket_response_dict = array_wrapper_of_switch_bracket_response_instance.to_dict()
# create an instance of ArrayWrapperOfSwitchBracketResponse from a dict
array_wrapper_of_switch_bracket_response_from_dict = ArrayWrapperOfSwitchBracketResponse.from_dict(array_wrapper_of_switch_bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


