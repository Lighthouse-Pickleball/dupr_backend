# ArrayWrapperSwitchBracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[SwitchBracketResponse]**](SwitchBracketResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_switch_bracket_response import ArrayWrapperSwitchBracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperSwitchBracketResponse from a JSON string
array_wrapper_switch_bracket_response_instance = ArrayWrapperSwitchBracketResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperSwitchBracketResponse.to_json())

# convert the object into a dict
array_wrapper_switch_bracket_response_dict = array_wrapper_switch_bracket_response_instance.to_dict()
# create an instance of ArrayWrapperSwitchBracketResponse from a dict
array_wrapper_switch_bracket_response_from_dict = ArrayWrapperSwitchBracketResponse.from_dict(array_wrapper_switch_bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


