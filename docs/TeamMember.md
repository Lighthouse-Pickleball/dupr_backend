# TeamMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**user_id** | **int** |  | 
**full_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**role** | **str** |  | 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.team_member import TeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMember from a JSON string
team_member_instance = TeamMember.from_json(json)
# print the JSON string representation of the object
print(TeamMember.to_json())

# convert the object into a dict
team_member_dict = team_member_instance.to_dict()
# create an instance of TeamMember from a dict
team_member_from_dict = TeamMember.from_dict(team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


