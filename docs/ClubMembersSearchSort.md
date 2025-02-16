# ClubMembersSearchSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** |  | [optional] 
**parameter** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.club_members_search_sort import ClubMembersSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMembersSearchSort from a JSON string
club_members_search_sort_instance = ClubMembersSearchSort.from_json(json)
# print the JSON string representation of the object
print(ClubMembersSearchSort.to_json())

# convert the object into a dict
club_members_search_sort_dict = club_members_search_sort_instance.to_dict()
# create an instance of ClubMembersSearchSort from a dict
club_members_search_sort_from_dict = ClubMembersSearchSort.from_dict(club_members_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


