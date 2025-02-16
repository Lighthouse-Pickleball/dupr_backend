# UserRestrictRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.user_restrict_request import UserRestrictRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRestrictRequest from a JSON string
user_restrict_request_instance = UserRestrictRequest.from_json(json)
# print the JSON string representation of the object
print UserRestrictRequest.to_json()

# convert the object into a dict
user_restrict_request_dict = user_restrict_request_instance.to_dict()
# create an instance of UserRestrictRequest from a dict
user_restrict_request_form_dict = user_restrict_request.from_dict(user_restrict_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


