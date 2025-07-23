# PaymentDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_status** | **str** |  | 
**is_club_member** | **bool** |  | 
**is_wait_listed** | **bool** |  | 
**refunded_amount** | **float** |  | 
**amount_paid** | **float** |  | 
**payment_capture** | **bool** |  | 
**player_status** | **str** |  | 
**is_registered** | **bool** |  | 
**event_fee** | **float** |  | 

## Example

```python
from dupr_backend.models.payment_details_response import PaymentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailsResponse from a JSON string
payment_details_response_instance = PaymentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentDetailsResponse.to_json())

# convert the object into a dict
payment_details_response_dict = payment_details_response_instance.to_dict()
# create an instance of PaymentDetailsResponse from a dict
payment_details_response_from_dict = PaymentDetailsResponse.from_dict(payment_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


