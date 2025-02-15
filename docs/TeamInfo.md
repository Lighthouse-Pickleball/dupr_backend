# TeamInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game1** | **int** |  | [optional] 
**game2** | **int** |  | [optional] 
**game3** | **int** |  | [optional] 
**game4** | **int** |  | [optional] 
**game5** | **int** |  | [optional] 
**player1_id** | **int** |  | [optional] 
**player2_id** | **int** |  | [optional] 
**winner** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.team_info import TeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfo from a JSON string
team_info_instance = TeamInfo.from_json(json)
# print the JSON string representation of the object
print(TeamInfo.to_json())

# convert the object into a dict
team_info_dict = team_info_instance.to_dict()
# create an instance of TeamInfo from a dict
team_info_from_dict = TeamInfo.from_dict(team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


