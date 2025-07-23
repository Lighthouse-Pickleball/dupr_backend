# StaffClubMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**club_id** | **int** |  | 
**role_id** | **int** |  | 
**approval** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**media_url** | **str** |  | [optional] 
**dupr_id** | **str** |  | 
**iso_alpha2_code** | **str** |  | 

## Example

```python
from dupr_backend.models.staff_club_member import StaffClubMember

# TODO update the JSON string below
json = "{}"
# create an instance of StaffClubMember from a JSON string
staff_club_member_instance = StaffClubMember.from_json(json)
# print the JSON string representation of the object
print(StaffClubMember.to_json())

# convert the object into a dict
staff_club_member_dict = staff_club_member_instance.to_dict()
# create an instance of StaffClubMember from a dict
staff_club_member_from_dict = StaffClubMember.from_dict(staff_club_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


