# StaffClubMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**role_id** | **int** |  | 
**club_id** | **int** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**iso_alpha2_code** | **str** |  | 

## Example

```python
from dupr_backend.models.staff_club_member_request import StaffClubMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaffClubMemberRequest from a JSON string
staff_club_member_request_instance = StaffClubMemberRequest.from_json(json)
# print the JSON string representation of the object
print(StaffClubMemberRequest.to_json())

# convert the object into a dict
staff_club_member_request_dict = staff_club_member_request_instance.to_dict()
# create an instance of StaffClubMemberRequest from a dict
staff_club_member_request_from_dict = StaffClubMemberRequest.from_dict(staff_club_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


