# TeamPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_substitution** | **bool** |  | 
**email** | **str** |  | 
**full_name** | **str** |  | 
**id** | **int** |  | 
**image_url** | **str** |  | [optional] 
**post_match_rating** | [**PostMatchRating**](PostMatchRating.md) |  | [optional] 
**referral_code** | **str** |  | [optional] 
**status** | **str** |  | 
**validated_match** | **bool** |  | [optional] 
**verified_email** | **bool** |  | 

## Example

```python
from dupr_backend.models.team_player import TeamPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPlayer from a JSON string
team_player_instance = TeamPlayer.from_json(json)
# print the JSON string representation of the object
print(TeamPlayer.to_json())

# convert the object into a dict
team_player_dict = team_player_instance.to_dict()
# create an instance of TeamPlayer from a dict
team_player_from_dict = TeamPlayer.from_dict(team_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


