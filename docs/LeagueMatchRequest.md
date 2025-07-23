# LeagueMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**venue** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**tournament** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**league** | **str** |  | [optional] 
**match_date** | **date** |  | 
**team1** | [**Team**](Team.md) |  | 
**team2** | [**Team**](Team.md) |  | 
**score_format_id** | **int** |  | [optional] 
**format** | **str** |  | 
**league_match_id** | **int** |  | 
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**league_id** | **int** |  | 

## Example

```python
from dupr_backend.models.league_match_request import LeagueMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueMatchRequest from a JSON string
league_match_request_instance = LeagueMatchRequest.from_json(json)
# print the JSON string representation of the object
print(LeagueMatchRequest.to_json())

# convert the object into a dict
league_match_request_dict = league_match_request_instance.to_dict()
# create an instance of LeagueMatchRequest from a dict
league_match_request_from_dict = LeagueMatchRequest.from_dict(league_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


