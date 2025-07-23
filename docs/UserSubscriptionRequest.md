# UserSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**cost** | **float** |  | 
**start_date** | **date** |  | 
**renewal_date** | **date** |  | 
**billing_period** | **str** |  | 
**is_active** | **bool** |  | 

## Example

```python
from dupr_backend.models.user_subscription_request import UserSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionRequest from a JSON string
user_subscription_request_instance = UserSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionRequest.to_json())

# convert the object into a dict
user_subscription_request_dict = user_subscription_request_instance.to_dict()
# create an instance of UserSubscriptionRequest from a dict
user_subscription_request_from_dict = UserSubscriptionRequest.from_dict(user_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


