# SubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[Subscription]**](Subscription.md) | A list of subscription descriptors. Descriptors will contain a list of operations and entitlements, which can be used to gate 3rd party features | 

## Example

```python
from dupr_backend.models.subscription_response import SubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponse from a JSON string
subscription_response_instance = SubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponse.to_json())

# convert the object into a dict
subscription_response_dict = subscription_response_instance.to_dict()
# create an instance of SubscriptionResponse from a dict
subscription_response_from_dict = SubscriptionResponse.from_dict(subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


