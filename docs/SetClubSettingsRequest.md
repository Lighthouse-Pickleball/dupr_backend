# SetClubSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 
**settings** | [**ClubSettings**](ClubSettings.md) |  | 

## Example

```python
from dupr_backend.models.set_club_settings_request import SetClubSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetClubSettingsRequest from a JSON string
set_club_settings_request_instance = SetClubSettingsRequest.from_json(json)
# print the JSON string representation of the object
print SetClubSettingsRequest.to_json()

# convert the object into a dict
set_club_settings_request_dict = set_club_settings_request_instance.to_dict()
# create an instance of SetClubSettingsRequest from a dict
set_club_settings_request_form_dict = set_club_settings_request.from_dict(set_club_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


