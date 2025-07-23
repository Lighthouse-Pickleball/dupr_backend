# ChangeEmailAdminRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_email** | **str** |  | 
**new_email** | **str** |  | 

## Example

```python
from dupr_backend.models.change_email_admin_request import ChangeEmailAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEmailAdminRequest from a JSON string
change_email_admin_request_instance = ChangeEmailAdminRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeEmailAdminRequest.to_json())

# convert the object into a dict
change_email_admin_request_dict = change_email_admin_request_instance.to_dict()
# create an instance of ChangeEmailAdminRequest from a dict
change_email_admin_request_from_dict = ChangeEmailAdminRequest.from_dict(change_email_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


