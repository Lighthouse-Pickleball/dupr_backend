# LeagueMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_match_id** | **int** |  | 
**match_id** | **int** |  | [optional] 
**registration_id** | **int** |  | 
**league_id** | **int** |  | 
**bracket_id** | **int** |  | 
**user_id** | **int** |  | [optional] 
**league_name** | **str** |  | 
**bracket_name** | **str** |  | 
**event_format** | **str** |  | 
**score_format** | [**ScoreFormatResponse**](ScoreFormatResponse.md) |  | 
**match_date** | **date** |  | 
**confirmed** | **bool** |  | 
**teams** | [**List[TeamResponse]**](TeamResponse.md) |  | 
**status** | **str** |  | [optional] 
**match_score_added** | **bool** |  | 
**league_match_status** | **str** |  | [optional] 
**round** | **int** |  | [optional] 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**venue** | **str** |  | 
**location** | **str** |  | 
**is_forfeited** | **bool** |  | 
**tag** | **str** |  | [optional] 
**in_queue** | **bool** |  | 
**no_of_games** | **int** |  | 
**tbd_1** | **int** |  | 
**tbd_2** | **int** |  | 
**match_slot** | **int** |  | 
**is_bye_match** | **bool** |  | 
**is_team_1_tbd** | **bool** |  | [optional] 
**is_team_2_tbd** | **bool** |  | [optional] 
**display_identity** | **str** |  | 
**is_next_round_confirmed** | **bool** |  | 
**impacted_draw** | **bool** |  | 
**forfeited** | **bool** |  | [optional] 
**bye_match** | **bool** |  | [optional] 
**next_round_confirmed** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.league_match_response import LeagueMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueMatchResponse from a JSON string
league_match_response_instance = LeagueMatchResponse.from_json(json)
# print the JSON string representation of the object
print(LeagueMatchResponse.to_json())

# convert the object into a dict
league_match_response_dict = league_match_response_instance.to_dict()
# create an instance of LeagueMatchResponse from a dict
league_match_response_from_dict = LeagueMatchResponse.from_dict(league_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


