# GetStripeSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 

## Example

```python
from dupr_backend.models.get_stripe_session_request import GetStripeSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStripeSessionRequest from a JSON string
get_stripe_session_request_instance = GetStripeSessionRequest.from_json(json)
# print the JSON string representation of the object
print(GetStripeSessionRequest.to_json())

# convert the object into a dict
get_stripe_session_request_dict = get_stripe_session_request_instance.to_dict()
# create an instance of GetStripeSessionRequest from a dict
get_stripe_session_request_from_dict = GetStripeSessionRequest.from_dict(get_stripe_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


