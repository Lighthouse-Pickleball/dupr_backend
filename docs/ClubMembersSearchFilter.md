# ClubMembersSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **str** |  | [optional] 
**age** | [**ClubMembersAgeFilter**](ClubMembersAgeFilter.md) |  | [optional] 
**rating** | [**ClubMembersRatingFilter**](ClubMembersRatingFilter.md) |  | [optional] 
**status** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**radius_in_meters** | **float** |  | [optional] 
**club_invitation_type** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.club_members_search_filter import ClubMembersSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMembersSearchFilter from a JSON string
club_members_search_filter_instance = ClubMembersSearchFilter.from_json(json)
# print the JSON string representation of the object
print(ClubMembersSearchFilter.to_json())

# convert the object into a dict
club_members_search_filter_dict = club_members_search_filter_instance.to_dict()
# create an instance of ClubMembersSearchFilter from a dict
club_members_search_filter_from_dict = ClubMembersSearchFilter.from_dict(club_members_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


