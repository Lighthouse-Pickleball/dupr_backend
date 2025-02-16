# MatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**club_id** | **int** |  | [optional] 
**confirmed** | **bool** |  | 
**created** | **str** |  | [optional] 
**creator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**display_identity** | **str** |  | 
**elo_calculated** | **bool** |  | [optional] 
**event_date** | **str** |  | 
**event_format** | **str** |  | 
**event_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**initialization** | **bool** |  | [optional] 
**league** | **str** |  | [optional] 
**league_id** | **int** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**location** | **str** |  | 
**match_id** | **int** |  | [optional] 
**match_score_added** | **bool** |  | 
**match_source** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**no_of_games** | **int** |  | [optional] 
**score_format** | [**ScoreFormatResponse**](ScoreFormatResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 
**teams** | [**List[TeamResponse]**](TeamResponse.md) |  | 
**tournament** | **str** |  | 
**user_id** | **int** |  | 
**validator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**venue** | **str** |  | 

## Example

```python
from dupr_backend.models.match_response import MatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchResponse from a JSON string
match_response_instance = MatchResponse.from_json(json)
# print the JSON string representation of the object
print MatchResponse.to_json()

# convert the object into a dict
match_response_dict = match_response_instance.to_dict()
# create an instance of MatchResponse from a dict
match_response_form_dict = match_response.from_dict(match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


