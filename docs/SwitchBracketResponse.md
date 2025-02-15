# SwitchBracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_reason** | **str** |  | [optional] 
**is_source_re_seeded** | **bool** |  | [optional] 
**is_success** | **bool** |  | [optional] 
**is_target_re_seeded** | **bool** |  | [optional] 
**registration_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.switch_bracket_response import SwitchBracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchBracketResponse from a JSON string
switch_bracket_response_instance = SwitchBracketResponse.from_json(json)
# print the JSON string representation of the object
print(SwitchBracketResponse.to_json())

# convert the object into a dict
switch_bracket_response_dict = switch_bracket_response_instance.to_dict()
# create an instance of SwitchBracketResponse from a dict
switch_bracket_response_from_dict = SwitchBracketResponse.from_dict(switch_bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


