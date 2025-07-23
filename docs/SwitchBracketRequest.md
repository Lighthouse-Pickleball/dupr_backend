# SwitchBracketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **int** |  | 
**source_bracket_id** | **int** |  | 
**target_bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**source_bracket_name** | **str** |  | 
**target_bracket_name** | **str** |  | 
**event_name** | **str** |  | 
**event_id** | **int** |  | 
**re_seed_bracket** | **bool** |  | 

## Example

```python
from dupr_backend.models.switch_bracket_request import SwitchBracketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchBracketRequest from a JSON string
switch_bracket_request_instance = SwitchBracketRequest.from_json(json)
# print the JSON string representation of the object
print(SwitchBracketRequest.to_json())

# convert the object into a dict
switch_bracket_request_dict = switch_bracket_request_instance.to_dict()
# create an instance of SwitchBracketRequest from a dict
switch_bracket_request_from_dict = SwitchBracketRequest.from_dict(switch_bracket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


