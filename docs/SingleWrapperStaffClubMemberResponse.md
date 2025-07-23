# SingleWrapperStaffClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**StaffClubMemberResponse**](StaffClubMemberResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_staff_club_member_response import SingleWrapperStaffClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperStaffClubMemberResponse from a JSON string
single_wrapper_staff_club_member_response_instance = SingleWrapperStaffClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperStaffClubMemberResponse.to_json())

# convert the object into a dict
single_wrapper_staff_club_member_response_dict = single_wrapper_staff_club_member_response_instance.to_dict()
# create an instance of SingleWrapperStaffClubMemberResponse from a dict
single_wrapper_staff_club_member_response_from_dict = SingleWrapperStaffClubMemberResponse.from_dict(single_wrapper_staff_club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


