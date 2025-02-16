# GetClientPermissionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | 

## Example

```python
from dupr_backend.models.get_client_permissions_request import GetClientPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientPermissionsRequest from a JSON string
get_client_permissions_request_instance = GetClientPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print GetClientPermissionsRequest.to_json()

# convert the object into a dict
get_client_permissions_request_dict = get_client_permissions_request_instance.to_dict()
# create an instance of GetClientPermissionsRequest from a dict
get_client_permissions_request_form_dict = get_client_permissions_request.from_dict(get_client_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


