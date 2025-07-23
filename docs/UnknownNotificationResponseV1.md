# UnknownNotificationResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urn** | [**Urn**](Urn.md) |  | [optional] 

## Example

```python
from dupr_backend.models.unknown_notification_response_v1 import UnknownNotificationResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownNotificationResponseV1 from a JSON string
unknown_notification_response_v1_instance = UnknownNotificationResponseV1.from_json(json)
# print the JSON string representation of the object
print(UnknownNotificationResponseV1.to_json())

# convert the object into a dict
unknown_notification_response_v1_dict = unknown_notification_response_v1_instance.to_dict()
# create an instance of UnknownNotificationResponseV1 from a dict
unknown_notification_response_v1_from_dict = UnknownNotificationResponseV1.from_dict(unknown_notification_response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


