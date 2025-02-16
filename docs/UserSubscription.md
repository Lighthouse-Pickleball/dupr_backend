# UserSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_period** | **str** |  | 
**cost** | **float** |  | 
**dupr_id** | **str** |  | 
**is_active** | **bool** |  | 
**renewal_date** | **str** |  | 
**start_date** | **str** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.user_subscription import UserSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscription from a JSON string
user_subscription_instance = UserSubscription.from_json(json)
# print the JSON string representation of the object
print UserSubscription.to_json()

# convert the object into a dict
user_subscription_dict = user_subscription_instance.to_dict()
# create an instance of UserSubscription from a dict
user_subscription_form_dict = user_subscription.from_dict(user_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


