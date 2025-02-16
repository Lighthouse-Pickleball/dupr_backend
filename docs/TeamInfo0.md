# TeamInfo0


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[PlayerInfo]**](PlayerInfo.md) |  | 
**team_no** | **int** |  | 

## Example

```python
from dupr_backend.models.team_info0 import TeamInfo0

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfo0 from a JSON string
team_info0_instance = TeamInfo0.from_json(json)
# print the JSON string representation of the object
print(TeamInfo0.to_json())

# convert the object into a dict
team_info0_dict = team_info0_instance.to_dict()
# create an instance of TeamInfo0 from a dict
team_info0_from_dict = TeamInfo0.from_dict(team_info0_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


