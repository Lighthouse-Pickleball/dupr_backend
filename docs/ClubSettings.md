# ClubSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_approve_join_requests** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.club_settings import ClubSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClubSettings from a JSON string
club_settings_instance = ClubSettings.from_json(json)
# print the JSON string representation of the object
print(ClubSettings.to_json())

# convert the object into a dict
club_settings_dict = club_settings_instance.to_dict()
# create an instance of ClubSettings from a dict
club_settings_from_dict = ClubSettings.from_dict(club_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


