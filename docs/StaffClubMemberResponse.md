# StaffClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directors** | [**List[StaffClubMember]**](StaffClubMember.md) |  | 
**max_director_count** | **int** |  | 
**max_organizer_count** | **int** |  | 
**organizers** | [**List[StaffClubMember]**](StaffClubMember.md) |  | 

## Example

```python
from dupr_backend.models.staff_club_member_response import StaffClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaffClubMemberResponse from a JSON string
staff_club_member_response_instance = StaffClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print(StaffClubMemberResponse.to_json())

# convert the object into a dict
staff_club_member_response_dict = staff_club_member_response_instance.to_dict()
# create an instance of StaffClubMemberResponse from a dict
staff_club_member_response_from_dict = StaffClubMemberResponse.from_dict(staff_club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


