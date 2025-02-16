# UserPreferencesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_email** | **bool** |  | [optional] 
**enable_newsletter** | **bool** |  | [optional] 
**enable_privacy** | **bool** |  | [optional] 
**enable_push** | **bool** |  | [optional] 
**enable_sms** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.user_preferences_request import UserPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserPreferencesRequest from a JSON string
user_preferences_request_instance = UserPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print UserPreferencesRequest.to_json()

# convert the object into a dict
user_preferences_request_dict = user_preferences_request_instance.to_dict()
# create an instance of UserPreferencesRequest from a dict
user_preferences_request_form_dict = user_preferences_request.from_dict(user_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


