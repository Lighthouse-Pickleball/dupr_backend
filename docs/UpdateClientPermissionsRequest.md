# UpdateClientPermissionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | 
**key_id** | **int** |  | 
**permissions** | [**List[Permission]**](Permission.md) | An optional list of permissions to assign to the client key | 

## Example

```python
from dupr_backend.models.update_client_permissions_request import UpdateClientPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientPermissionsRequest from a JSON string
update_client_permissions_request_instance = UpdateClientPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateClientPermissionsRequest.to_json()

# convert the object into a dict
update_client_permissions_request_dict = update_client_permissions_request_instance.to_dict()
# create an instance of UpdateClientPermissionsRequest from a dict
update_client_permissions_request_form_dict = update_client_permissions_request.from_dict(update_client_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


