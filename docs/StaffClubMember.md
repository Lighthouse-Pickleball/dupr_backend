# StaffClubMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval** | **str** |  | 
**club_id** | **int** |  | 
**dupr_id** | **str** |  | 
**email** | **str** |  | 
**iso_alpha2_code** | **str** |  | 
**media_url** | **str** |  | [optional] 
**name** | **str** |  | 
**phone** | **str** |  | [optional] 
**role_id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.staff_club_member import StaffClubMember

# TODO update the JSON string below
json = "{}"
# create an instance of StaffClubMember from a JSON string
staff_club_member_instance = StaffClubMember.from_json(json)
# print the JSON string representation of the object
print StaffClubMember.to_json()

# convert the object into a dict
staff_club_member_dict = staff_club_member_instance.to_dict()
# create an instance of StaffClubMember from a dict
staff_club_member_form_dict = staff_club_member.from_dict(staff_club_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


