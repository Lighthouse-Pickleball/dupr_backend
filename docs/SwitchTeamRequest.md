# SwitchTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**event_id** | **int** |  | 
**event_name** | **str** |  | 
**player1** | **int** |  | 
**player2** | **int** |  | 
**re_seed_bracket** | **bool** |  | [optional] 
**registration_id** | **int** |  | 
**source_bracket_id** | **int** |  | 
**source_bracket_name** | **str** |  | 
**target_bracket_id** | **int** |  | 
**target_bracket_name** | **str** |  | 

## Example

```python
from dupr_backend.models.switch_team_request import SwitchTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchTeamRequest from a JSON string
switch_team_request_instance = SwitchTeamRequest.from_json(json)
# print the JSON string representation of the object
print(SwitchTeamRequest.to_json())

# convert the object into a dict
switch_team_request_dict = switch_team_request_instance.to_dict()
# create an instance of SwitchTeamRequest from a dict
switch_team_request_from_dict = SwitchTeamRequest.from_dict(switch_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


