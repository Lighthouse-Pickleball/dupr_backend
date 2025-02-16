# CreateNewTeamRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**player1** | **int** |  | 
**player2** | **int** |  | 

## Example

```python
from dupr_backend.models.create_new_team_request import CreateNewTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewTeamRequest from a JSON string
create_new_team_request_instance = CreateNewTeamRequest.from_json(json)
# print the JSON string representation of the object
print CreateNewTeamRequest.to_json()

# convert the object into a dict
create_new_team_request_dict = create_new_team_request_instance.to_dict()
# create an instance of CreateNewTeamRequest from a dict
create_new_team_request_form_dict = create_new_team_request.from_dict(create_new_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


