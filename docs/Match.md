# Match


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**venue** | **str** |  | [optional] 
**location** | **str** |  | 
**match_score_added** | **bool** |  | 
**tournament** | **str** |  | [optional] 
**league** | **str** |  | [optional] 
**event_date** | **date** |  | 
**event_format** | **str** |  | 
**score_format** | [**ScoreFormat**](ScoreFormat.md) |  | [optional] 
**confirmed** | **bool** |  | 
**confirmation_threshold** | **int** |  | 
**teams** | [**List[Team]**](Team.md) |  | 
**status** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**event** | **str** |  | [optional] 
**match_source** | **str** |  | [optional] 
**club_id** | **int** |  | [optional] 
**league_id** | **int** |  | [optional] 
**bracket_id** | **int** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**match_type** | **str** |  | [optional] 
**used_in_initialization** | **bool** |  | 
**elo_calculated** | **bool** |  | [optional] 
**validator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**creator** | [**BasicUserInfo**](BasicUserInfo.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**club_name** | **str** |  | [optional] 
**client_name** | **str** |  | [optional] 
**is_pro_match** | **bool** |  | 
**player_ids** | **List[int]** |  | 
**is_elo_rated_match** | **bool** |  | 
**is_pre_elo_match** | **bool** |  | 

## Example

```python
from dupr_backend.models.match import Match

# TODO update the JSON string below
json = "{}"
# create an instance of Match from a JSON string
match_instance = Match.from_json(json)
# print the JSON string representation of the object
print(Match.to_json())

# convert the object into a dict
match_dict = match_instance.to_dict()
# create an instance of Match from a dict
match_from_dict = Match.from_dict(match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


