# LeagueMatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**bracket_name** | **str** |  | 
**confirmed** | **bool** |  | [optional] 
**display_identity** | **str** |  | 
**end_date** | **str** |  | 
**event_format** | **str** |  | 
**impacted_draw** | **bool** |  | 
**in_queue** | **bool** |  | [optional] 
**is_bye_match** | **bool** |  | 
**is_forfeited** | **bool** |  | [optional] 
**is_next_round_confirmed** | **bool** |  | 
**is_team_1_tbd** | **bool** |  | [optional] 
**is_team_2_tbd** | **bool** |  | [optional] 
**league_id** | **int** |  | 
**league_match_id** | **int** |  | 
**league_match_status** | **str** |  | [optional] 
**league_name** | **str** |  | 
**location** | **str** |  | 
**match_date** | **str** |  | 
**match_id** | **int** |  | [optional] 
**match_score_added** | **bool** |  | [optional] 
**match_slot** | **int** |  | 
**no_of_games** | **int** |  | [optional] 
**registration_id** | **int** |  | 
**round** | **int** |  | [optional] 
**score_format** | [**ScoreFormatResponse**](ScoreFormatResponse.md) |  | 
**start_date** | **str** |  | 
**status** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**tbd_1** | **int** |  | 
**tbd_2** | **int** |  | 
**teams** | [**List[TeamResponse]**](TeamResponse.md) |  | 
**user_id** | **int** |  | [optional] 
**venue** | **str** |  | 

## Example

```python
from dupr_backend.models.league_match_response import LeagueMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueMatchResponse from a JSON string
league_match_response_instance = LeagueMatchResponse.from_json(json)
# print the JSON string representation of the object
print LeagueMatchResponse.to_json()

# convert the object into a dict
league_match_response_dict = league_match_response_instance.to_dict()
# create an instance of LeagueMatchResponse from a dict
league_match_response_form_dict = league_match_response.from_dict(league_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


