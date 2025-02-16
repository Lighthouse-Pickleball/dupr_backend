# ClubMembersSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[int]** |  | [optional] 
**filter** | [**ClubMembersSearchFilter**](ClubMembersSearchFilter.md) |  | [optional] 
**include_pending_players** | **bool** |  | [optional] 
**include_staff** | **bool** |  | [optional] 
**limit** | **int** |  | 
**offset** | **int** |  | 
**query** | **str** |  | 
**sort** | [**ClubMembersSearchSort**](ClubMembersSearchSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMembersSearchRequest from a JSON string
club_members_search_request_instance = ClubMembersSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ClubMembersSearchRequest.to_json())

# convert the object into a dict
club_members_search_request_dict = club_members_search_request_instance.to_dict()
# create an instance of ClubMembersSearchRequest from a dict
club_members_search_request_from_dict = ClubMembersSearchRequest.from_dict(club_members_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


