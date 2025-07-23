# MatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**match_id** | **int** |  | [optional] 
**user_id** | **int** |  | 
**display_identity** | **str** |  | 
**venue** | **str** |  | 
**location** | **str** |  | 
**match_score_added** | **bool** |  | 
**tournament** | **str** |  | 
**league** | **str** |  | [optional] 
**event_date** | **date** |  | 
**event_format** | **str** |  | 
**score_format** | [**ScoreFormatResponse**](ScoreFormatResponse.md) |  | [optional] 
**confirmed** | **bool** |  | 
**teams** | [**List[TeamResponse]**](TeamResponse.md) |  | 
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**event_name** | **str** |  | [optional] 
**match_source** | **str** |  | [optional] 
**club_id** | **int** |  | [optional] 
**league_id** | **int** |  | [optional] 
**bracket_id** | **int** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**no_of_games** | **int** |  | 
**status** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**elo_calculated** | **bool** |  | [optional] 
**initialization** | **bool** |  | [optional] 
**validator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**creator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**client_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.match_response import MatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchResponse from a JSON string
match_response_instance = MatchResponse.from_json(json)
# print the JSON string representation of the object
print(MatchResponse.to_json())

# convert the object into a dict
match_response_dict = match_response_instance.to_dict()
# create an instance of MatchResponse from a dict
match_response_from_dict = MatchResponse.from_dict(match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


