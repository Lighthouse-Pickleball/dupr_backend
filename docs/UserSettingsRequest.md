# UserSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **Dict[str, str]** |  | 

## Example

```python
from dupr_backend.models.user_settings_request import UserSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsRequest from a JSON string
user_settings_request_instance = UserSettingsRequest.from_json(json)
# print the JSON string representation of the object
print UserSettingsRequest.to_json()

# convert the object into a dict
user_settings_request_dict = user_settings_request_instance.to_dict()
# create an instance of UserSettingsRequest from a dict
user_settings_request_form_dict = user_settings_request.from_dict(user_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


