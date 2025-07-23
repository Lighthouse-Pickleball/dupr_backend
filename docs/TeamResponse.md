# TeamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**serial** | **int** |  | 
**player1** | [**TeamPlayerResponse**](TeamPlayerResponse.md) |  | 
**player2** | [**TeamPlayerResponse**](TeamPlayerResponse.md) |  | [optional] 
**game1** | **int** |  | 
**game2** | **int** |  | 
**game3** | **int** |  | 
**game4** | **int** |  | 
**game5** | **int** |  | 
**winner** | **bool** |  | 
**delta** | **str** |  | 
**team_rating** | **str** |  | 
**pre_match_rating_and_impact** | [**PreMatchRatingAndImpact**](PreMatchRatingAndImpact.md) |  | 

## Example

```python
from dupr_backend.models.team_response import TeamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamResponse from a JSON string
team_response_instance = TeamResponse.from_json(json)
# print the JSON string representation of the object
print(TeamResponse.to_json())

# convert the object into a dict
team_response_dict = team_response_instance.to_dict()
# create an instance of TeamResponse from a dict
team_response_from_dict = TeamResponse.from_dict(team_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


