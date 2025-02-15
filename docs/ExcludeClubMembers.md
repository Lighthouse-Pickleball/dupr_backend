# ExcludeClubMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.exclude_club_members import ExcludeClubMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ExcludeClubMembers from a JSON string
exclude_club_members_instance = ExcludeClubMembers.from_json(json)
# print the JSON string representation of the object
print(ExcludeClubMembers.to_json())

# convert the object into a dict
exclude_club_members_dict = exclude_club_members_instance.to_dict()
# create an instance of ExcludeClubMembers from a dict
exclude_club_members_from_dict = ExcludeClubMembers.from_dict(exclude_club_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


