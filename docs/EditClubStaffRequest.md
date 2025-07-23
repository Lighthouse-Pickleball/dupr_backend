# EditClubStaffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**operation** | **str** |  | 
**user_id** | **int** |  | 
**rol_id** | **int** |  | 
**delete_user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.edit_club_staff_request import EditClubStaffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditClubStaffRequest from a JSON string
edit_club_staff_request_instance = EditClubStaffRequest.from_json(json)
# print the JSON string representation of the object
print(EditClubStaffRequest.to_json())

# convert the object into a dict
edit_club_staff_request_dict = edit_club_staff_request_instance.to_dict()
# create an instance of EditClubStaffRequest from a dict
edit_club_staff_request_from_dict = EditClubStaffRequest.from_dict(edit_club_staff_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


