# NotificationHistoryResponseDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_v1** | [**ClubV1**](ClubV1.md) |  | 
**get_stream_comment_v1** | [**GetStreamCommentResponseV1Urn**](GetStreamCommentResponseV1Urn.md) |  | 
**get_stream_post_v1** | [**GetStreamPostResponseV1Urn**](GetStreamPostResponseV1Urn.md) |  | 
**timestamp** | [**TimestampResponseAllOfTimestamp**](TimestampResponseAllOfTimestamp.md) |  | 
**urn** | [**Urn**](Urn.md) |  | [optional] 
**user_v1** | [**UserV1**](UserV1.md) |  | 

## Example

```python
from dupr_backend.models.notification_history_response_data_value import NotificationHistoryResponseDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationHistoryResponseDataValue from a JSON string
notification_history_response_data_value_instance = NotificationHistoryResponseDataValue.from_json(json)
# print the JSON string representation of the object
print(NotificationHistoryResponseDataValue.to_json())

# convert the object into a dict
notification_history_response_data_value_dict = notification_history_response_data_value_instance.to_dict()
# create an instance of NotificationHistoryResponseDataValue from a dict
notification_history_response_data_value_from_dict = NotificationHistoryResponseDataValue.from_dict(notification_history_response_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


