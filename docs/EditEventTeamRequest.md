# EditEventTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**bracket_id** | **int** |  | 
**registration_id** | **int** |  | 
**player1** | **int** |  | 
**player2** | **int** |  | 
**is_player1_club_member** | **bool** |  | 
**is_player2_club_member** | **bool** |  | 

## Example

```python
from dupr_backend.models.edit_event_team_request import EditEventTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditEventTeamRequest from a JSON string
edit_event_team_request_instance = EditEventTeamRequest.from_json(json)
# print the JSON string representation of the object
print(EditEventTeamRequest.to_json())

# convert the object into a dict
edit_event_team_request_dict = edit_event_team_request_instance.to_dict()
# create an instance of EditEventTeamRequest from a dict
edit_event_team_request_from_dict = EditEventTeamRequest.from_dict(edit_event_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


