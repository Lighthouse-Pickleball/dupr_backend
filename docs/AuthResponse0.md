# AuthResponse0


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | 

## Example

```python
from dupr_backend.models.auth_response0 import AuthResponse0

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResponse0 from a JSON string
auth_response0_instance = AuthResponse0.from_json(json)
# print the JSON string representation of the object
print(AuthResponse0.to_json())

# convert the object into a dict
auth_response0_dict = auth_response0_instance.to_dict()
# create an instance of AuthResponse0 from a dict
auth_response0_from_dict = AuthResponse0.from_dict(auth_response0_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


