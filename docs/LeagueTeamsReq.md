# LeagueTeamsReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_status** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 
**player1** | [**PlayerReq**](PlayerReq.md) |  | [optional] 
**player2** | [**PlayerReq**](PlayerReq.md) |  | [optional] 
**registration_id** | **int** |  | [optional] 
**team_status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_teams_req import LeagueTeamsReq

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueTeamsReq from a JSON string
league_teams_req_instance = LeagueTeamsReq.from_json(json)
# print the JSON string representation of the object
print(LeagueTeamsReq.to_json())

# convert the object into a dict
league_teams_req_dict = league_teams_req_instance.to_dict()
# create an instance of LeagueTeamsReq from a dict
league_teams_req_from_dict = LeagueTeamsReq.from_dict(league_teams_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


