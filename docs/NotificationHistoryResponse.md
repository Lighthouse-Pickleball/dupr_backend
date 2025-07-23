# NotificationHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**data** | [**Dict[str, NotificationHistoryResponseDataValue]**](NotificationHistoryResponseDataValue.md) |  | 

## Example

```python
from dupr_backend.models.notification_history_response import NotificationHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationHistoryResponse from a JSON string
notification_history_response_instance = NotificationHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationHistoryResponse.to_json())

# convert the object into a dict
notification_history_response_dict = notification_history_response_instance.to_dict()
# create an instance of NotificationHistoryResponse from a dict
notification_history_response_from_dict = NotificationHistoryResponse.from_dict(notification_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


