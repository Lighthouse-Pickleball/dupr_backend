# TeamUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**player1** | **int** |  | 
**player2** | **int** |  | [optional] 
**game1** | **int** |  | [optional] 
**game2** | **int** |  | [optional] 
**game3** | **int** |  | [optional] 
**game4** | **int** |  | [optional] 
**game5** | **int** |  | [optional] 
**winner** | **bool** |  | [optional] 
**player_ids** | **List[int]** |  | 

## Example

```python
from dupr_backend.models.team_update_request import TeamUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUpdateRequest from a JSON string
team_update_request_instance = TeamUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TeamUpdateRequest.to_json())

# convert the object into a dict
team_update_request_dict = team_update_request_instance.to_dict()
# create an instance of TeamUpdateRequest from a dict
team_update_request_from_dict = TeamUpdateRequest.from_dict(team_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


