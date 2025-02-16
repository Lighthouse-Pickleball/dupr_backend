# ClubRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_status** | **str** |  | 
**club_id** | **int** |  | 
**created** | **str** |  | [optional] 
**join_type** | **str** |  | [optional] 
**request_by** | **int** |  | [optional] 
**role** | **str** |  | 
**role_id** | **int** |  | 

## Example

```python
from dupr_backend.models.club_role import ClubRole

# TODO update the JSON string below
json = "{}"
# create an instance of ClubRole from a JSON string
club_role_instance = ClubRole.from_json(json)
# print the JSON string representation of the object
print(ClubRole.to_json())

# convert the object into a dict
club_role_dict = club_role_instance.to_dict()
# create an instance of ClubRole from a dict
club_role_from_dict = ClubRole.from_dict(club_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


