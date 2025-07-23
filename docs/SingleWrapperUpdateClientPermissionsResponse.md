# SingleWrapperUpdateClientPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**UpdateClientPermissionsResponse**](UpdateClientPermissionsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_update_client_permissions_response import SingleWrapperUpdateClientPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperUpdateClientPermissionsResponse from a JSON string
single_wrapper_update_client_permissions_response_instance = SingleWrapperUpdateClientPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperUpdateClientPermissionsResponse.to_json())

# convert the object into a dict
single_wrapper_update_client_permissions_response_dict = single_wrapper_update_client_permissions_response_instance.to_dict()
# create an instance of SingleWrapperUpdateClientPermissionsResponse from a dict
single_wrapper_update_client_permissions_response_from_dict = SingleWrapperUpdateClientPermissionsResponse.from_dict(single_wrapper_update_client_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


