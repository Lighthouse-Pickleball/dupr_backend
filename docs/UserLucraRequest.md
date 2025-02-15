# UserLucraRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lucra_connected** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.user_lucra_request import UserLucraRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserLucraRequest from a JSON string
user_lucra_request_instance = UserLucraRequest.from_json(json)
# print the JSON string representation of the object
print(UserLucraRequest.to_json())

# convert the object into a dict
user_lucra_request_dict = user_lucra_request_instance.to_dict()
# create an instance of UserLucraRequest from a dict
user_lucra_request_from_dict = UserLucraRequest.from_dict(user_lucra_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


