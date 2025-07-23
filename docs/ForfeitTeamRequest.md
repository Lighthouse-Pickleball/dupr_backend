# ForfeitTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**player1** | **int** |  | 
**player2** | **int** |  | [optional] 
**is_forfeited** | **bool** |  | 

## Example

```python
from dupr_backend.models.forfeit_team_request import ForfeitTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForfeitTeamRequest from a JSON string
forfeit_team_request_instance = ForfeitTeamRequest.from_json(json)
# print the JSON string representation of the object
print(ForfeitTeamRequest.to_json())

# convert the object into a dict
forfeit_team_request_dict = forfeit_team_request_instance.to_dict()
# create an instance of ForfeitTeamRequest from a dict
forfeit_team_request_from_dict = ForfeitTeamRequest.from_dict(forfeit_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


