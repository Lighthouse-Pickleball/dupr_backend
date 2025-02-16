# VerifiedMatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 
**event_date** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**team_a_player1** | **str** |  | [optional] 
**team_a_player1_id** | **str** |  | [optional] 
**team_a_player2** | **str** |  | [optional] 
**team_a_player2_id** | **str** |  | [optional] 
**team_a_points_game1** | **int** |  | [optional] 
**team_a_points_game2** | **int** |  | [optional] 
**team_a_points_game3** | **int** |  | [optional] 
**team_a_points_game4** | **int** |  | [optional] 
**team_a_points_game5** | **int** |  | [optional] 
**team_b_player1** | **str** |  | [optional] 
**team_b_player1_id** | **str** |  | [optional] 
**team_b_player2** | **str** |  | [optional] 
**team_b_player2_id** | **str** |  | [optional] 
**team_b_points_game1** | **int** |  | [optional] 
**team_b_points_game2** | **int** |  | [optional] 
**team_b_points_game3** | **int** |  | [optional] 
**team_b_points_game4** | **int** |  | [optional] 
**team_b_points_game5** | **int** |  | [optional] 
**tournament_name** | **str** |  | [optional] 
**venue** | **str** |  | [optional] 
**winning_team** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.verified_match_request import VerifiedMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedMatchRequest from a JSON string
verified_match_request_instance = VerifiedMatchRequest.from_json(json)
# print the JSON string representation of the object
print VerifiedMatchRequest.to_json()

# convert the object into a dict
verified_match_request_dict = verified_match_request_instance.to_dict()
# create an instance of VerifiedMatchRequest from a dict
verified_match_request_form_dict = verified_match_request.from_dict(verified_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


