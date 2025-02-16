# UserSubscriptionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_period** | **str** |  | 
**cost** | **float** |  | 
**is_active** | **bool** |  | 
**renewal_date** | **str** |  | 
**start_date** | **str** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.user_subscription_request import UserSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionRequest from a JSON string
user_subscription_request_instance = UserSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print UserSubscriptionRequest.to_json()

# convert the object into a dict
user_subscription_request_dict = user_subscription_request_instance.to_dict()
# create an instance of UserSubscriptionRequest from a dict
user_subscription_request_form_dict = user_subscription_request.from_dict(user_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


