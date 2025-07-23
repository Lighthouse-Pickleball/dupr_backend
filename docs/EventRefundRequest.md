# EventRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**event_id** | **int** |  | 
**event_name** | **str** |  | 
**process_refund** | **bool** |  | 
**refund_amount** | **float** |  | 
**player_id** | **int** |  | 
**brackets** | [**List[BracketRefundRequest]**](BracketRefundRequest.md) |  | 

## Example

```python
from dupr_backend.models.event_refund_request import EventRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventRefundRequest from a JSON string
event_refund_request_instance = EventRefundRequest.from_json(json)
# print the JSON string representation of the object
print(EventRefundRequest.to_json())

# convert the object into a dict
event_refund_request_dict = event_refund_request_instance.to_dict()
# create an instance of EventRefundRequest from a dict
event_refund_request_from_dict = EventRefundRequest.from_dict(event_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


