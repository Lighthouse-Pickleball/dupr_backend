# SingleWrapperOfStaffClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**StaffClubMemberResponse**](StaffClubMemberResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_staff_club_member_response import SingleWrapperOfStaffClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfStaffClubMemberResponse from a JSON string
single_wrapper_of_staff_club_member_response_instance = SingleWrapperOfStaffClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfStaffClubMemberResponse.to_json())

# convert the object into a dict
single_wrapper_of_staff_club_member_response_dict = single_wrapper_of_staff_club_member_response_instance.to_dict()
# create an instance of SingleWrapperOfStaffClubMemberResponse from a dict
single_wrapper_of_staff_club_member_response_from_dict = SingleWrapperOfStaffClubMemberResponse.from_dict(single_wrapper_of_staff_club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


