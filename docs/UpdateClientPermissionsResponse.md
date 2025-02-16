# UpdateClientPermissionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | 
**key_id** | **int** |  | 

## Example

```python
from dupr_backend.models.update_client_permissions_response import UpdateClientPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientPermissionsResponse from a JSON string
update_client_permissions_response_instance = UpdateClientPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print UpdateClientPermissionsResponse.to_json()

# convert the object into a dict
update_client_permissions_response_dict = update_client_permissions_response_instance.to_dict()
# create an instance of UpdateClientPermissionsResponse from a dict
update_client_permissions_response_form_dict = update_client_permissions_response.from_dict(update_client_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


