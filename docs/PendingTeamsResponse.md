# PendingTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_source** | [**LeagueTeamsResponse**](LeagueTeamsResponse.md) |  | 
**team_target** | [**LeagueTeamsResponse**](LeagueTeamsResponse.md) |  | 

## Example

```python
from dupr_backend.models.pending_teams_response import PendingTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PendingTeamsResponse from a JSON string
pending_teams_response_instance = PendingTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(PendingTeamsResponse.to_json())

# convert the object into a dict
pending_teams_response_dict = pending_teams_response_instance.to_dict()
# create an instance of PendingTeamsResponse from a dict
pending_teams_response_from_dict = PendingTeamsResponse.from_dict(pending_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


