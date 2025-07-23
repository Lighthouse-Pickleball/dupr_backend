# BracketPlayerSwitchWaitListedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**team_source** | [**Team**](Team.md) |  | 
**team_target** | [**Team**](Team.md) |  | 

## Example

```python
from dupr_backend.models.bracket_player_switch_wait_listed_request import BracketPlayerSwitchWaitListedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BracketPlayerSwitchWaitListedRequest from a JSON string
bracket_player_switch_wait_listed_request_instance = BracketPlayerSwitchWaitListedRequest.from_json(json)
# print the JSON string representation of the object
print(BracketPlayerSwitchWaitListedRequest.to_json())

# convert the object into a dict
bracket_player_switch_wait_listed_request_dict = bracket_player_switch_wait_listed_request_instance.to_dict()
# create an instance of BracketPlayerSwitchWaitListedRequest from a dict
bracket_player_switch_wait_listed_request_from_dict = BracketPlayerSwitchWaitListedRequest.from_dict(bracket_player_switch_wait_listed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


