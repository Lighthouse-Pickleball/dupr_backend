# PaymentReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_key** | **str** |  | 
**purchased_package** | **str** |  | 

## Example

```python
from dupr_backend.models.payment_report_request import PaymentReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReportRequest from a JSON string
payment_report_request_instance = PaymentReportRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentReportRequest.to_json())

# convert the object into a dict
payment_report_request_dict = payment_report_request_instance.to_dict()
# create an instance of PaymentReportRequest from a dict
payment_report_request_from_dict = PaymentReportRequest.from_dict(payment_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


