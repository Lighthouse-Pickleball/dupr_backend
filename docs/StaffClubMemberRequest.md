# StaffClubMemberRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**email** | **str** |  | 
**iso_alpha2_code** | **str** |  | 
**name** | **str** |  | 
**phone** | **str** |  | [optional] 
**role_id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.staff_club_member_request import StaffClubMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaffClubMemberRequest from a JSON string
staff_club_member_request_instance = StaffClubMemberRequest.from_json(json)
# print the JSON string representation of the object
print StaffClubMemberRequest.to_json()

# convert the object into a dict
staff_club_member_request_dict = staff_club_member_request_instance.to_dict()
# create an instance of StaffClubMemberRequest from a dict
staff_club_member_request_form_dict = staff_club_member_request.from_dict(staff_club_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


