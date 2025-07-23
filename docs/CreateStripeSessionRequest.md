# CreateStripeSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_key** | **str** |  | 
**return_url** | **str** |  | 
**success_url** | **str** |  | [optional] 
**canceled_url** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.create_stripe_session_request import CreateStripeSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeSessionRequest from a JSON string
create_stripe_session_request_instance = CreateStripeSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStripeSessionRequest.to_json())

# convert the object into a dict
create_stripe_session_request_dict = create_stripe_session_request_instance.to_dict()
# create an instance of CreateStripeSessionRequest from a dict
create_stripe_session_request_from_dict = CreateStripeSessionRequest.from_dict(create_stripe_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


