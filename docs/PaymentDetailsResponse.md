# PaymentDetailsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_paid** | **float** |  | 
**event_fee** | **float** |  | 
**is_club_member** | **bool** |  | 
**is_registered** | **bool** |  | 
**is_wait_listed** | **bool** |  | 
**payment_capture** | **bool** |  | 
**payment_status** | **str** |  | 
**player_status** | **str** |  | 
**refunded_amount** | **float** |  | 

## Example

```python
from dupr_backend.models.payment_details_response import PaymentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailsResponse from a JSON string
payment_details_response_instance = PaymentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print PaymentDetailsResponse.to_json()

# convert the object into a dict
payment_details_response_dict = payment_details_response_instance.to_dict()
# create an instance of PaymentDetailsResponse from a dict
payment_details_response_form_dict = payment_details_response.from_dict(payment_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


