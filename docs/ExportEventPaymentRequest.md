# ExportEventPaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | [optional] 
**league_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.export_event_payment_request import ExportEventPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportEventPaymentRequest from a JSON string
export_event_payment_request_instance = ExportEventPaymentRequest.from_json(json)
# print the JSON string representation of the object
print ExportEventPaymentRequest.to_json()

# convert the object into a dict
export_event_payment_request_dict = export_event_payment_request_instance.to_dict()
# create an instance of ExportEventPaymentRequest from a dict
export_event_payment_request_form_dict = export_event_payment_request.from_dict(export_event_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


