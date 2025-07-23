# SwitchTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_id** | **int** |  | 
**player1** | **int** |  | 
**player2** | **int** |  | 
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


