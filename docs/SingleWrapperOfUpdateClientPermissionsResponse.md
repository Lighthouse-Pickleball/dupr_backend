# SingleWrapperOfUpdateClientPermissionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**UpdateClientPermissionsResponse**](UpdateClientPermissionsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_update_client_permissions_response import SingleWrapperOfUpdateClientPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfUpdateClientPermissionsResponse from a JSON string
single_wrapper_of_update_client_permissions_response_instance = SingleWrapperOfUpdateClientPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfUpdateClientPermissionsResponse.to_json()

# convert the object into a dict
single_wrapper_of_update_client_permissions_response_dict = single_wrapper_of_update_client_permissions_response_instance.to_dict()
# create an instance of SingleWrapperOfUpdateClientPermissionsResponse from a dict
single_wrapper_of_update_client_permissions_response_form_dict = single_wrapper_of_update_client_permissions_response.from_dict(single_wrapper_of_update_client_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


