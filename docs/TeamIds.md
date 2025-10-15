# TeamIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player1_id** | **int** |  | 
**player2_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.team_ids import TeamIds

# TODO update the JSON string below
json = "{}"
# create an instance of TeamIds from a JSON string
team_ids_instance = TeamIds.from_json(json)
# print the JSON string representation of the object
print(TeamIds.to_json())

# convert the object into a dict
team_ids_dict = team_ids_instance.to_dict()
# create an instance of TeamIds from a dict
team_ids_from_dict = TeamIds.from_dict(team_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


