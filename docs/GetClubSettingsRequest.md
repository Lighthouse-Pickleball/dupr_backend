# GetClubSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.get_club_settings_request import GetClubSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetClubSettingsRequest from a JSON string
get_club_settings_request_instance = GetClubSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(GetClubSettingsRequest.to_json())

# convert the object into a dict
get_club_settings_request_dict = get_club_settings_request_instance.to_dict()
# create an instance of GetClubSettingsRequest from a dict
get_club_settings_request_from_dict = GetClubSettingsRequest.from_dict(get_club_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


