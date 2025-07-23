# TeamPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**full_name** | **str** |  | 
**dupr_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**allow_substitution** | **bool** |  | 
**post_match_rating** | [**PostMatchRating**](PostMatchRating.md) |  | [optional] 
**validated_match** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.team_player_response import TeamPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPlayerResponse from a JSON string
team_player_response_instance = TeamPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(TeamPlayerResponse.to_json())

# convert the object into a dict
team_player_response_dict = team_player_response_instance.to_dict()
# create an instance of TeamPlayerResponse from a dict
team_player_response_from_dict = TeamPlayerResponse.from_dict(team_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


