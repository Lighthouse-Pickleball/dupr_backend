# Match


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**club_id** | **int** |  | [optional] 
**confirmation_threshold** | **int** |  | 
**confirmed** | **bool** |  | 
**created** | **datetime** |  | [optional] 
**creator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**elo_calculated** | **bool** |  | [optional] 
**elo_rated_match** | **bool** |  | 
**event** | **str** |  | [optional] 
**event_date** | **date** |  | 
**event_format** | **str** |  | 
**id** | **int** |  | [optional] 
**league** | **str** |  | [optional] 
**league_id** | **int** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**location** | **str** |  | 
**match_score_added** | **bool** |  | 
**match_source** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**player_ids** | **List[int]** |  | 
**pre_elo_match** | **bool** |  | 
**pro_match** | **bool** |  | 
**score_format** | [**ScoreFormat**](ScoreFormat.md) |  | [optional] 
**status** | **str** |  | [optional] 
**teams** | [**List[Team]**](Team.md) |  | 
**tournament** | **str** |  | [optional] 
**used_in_initialization** | **bool** |  | 
**user_id** | **int** |  | [optional] 
**validator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**venue** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.match import Match

# TODO update the JSON string below
json = "{}"
# create an instance of Match from a JSON string
match_instance = Match.from_json(json)
# print the JSON string representation of the object
print Match.to_json()

# convert the object into a dict
match_dict = match_instance.to_dict()
# create an instance of Match from a dict
match_form_dict = match.from_dict(match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


