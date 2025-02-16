# UserAuthProviderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facebook** | [**FacebookRequest**](FacebookRequest.md) |  | [optional] 
**instagram** | [**InstagramRequest**](InstagramRequest.md) |  | [optional] 

## Example

```python
from dupr_backend.models.user_auth_provider_request import UserAuthProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAuthProviderRequest from a JSON string
user_auth_provider_request_instance = UserAuthProviderRequest.from_json(json)
# print the JSON string representation of the object
print UserAuthProviderRequest.to_json()

# convert the object into a dict
user_auth_provider_request_dict = user_auth_provider_request_instance.to_dict()
# create an instance of UserAuthProviderRequest from a dict
user_auth_provider_request_form_dict = user_auth_provider_request.from_dict(user_auth_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


