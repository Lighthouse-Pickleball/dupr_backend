# UserSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**dupr_id** | **str** |  | 
**cost** | **float** |  | 
**billing_period** | **str** |  | 
**start_date** | **date** |  | 
**renewal_date** | **date** |  | 
**is_active** | **bool** |  | 

## Example

```python
from dupr_backend.models.user_subscription import UserSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscription from a JSON string
user_subscription_instance = UserSubscription.from_json(json)
# print the JSON string representation of the object
print(UserSubscription.to_json())

# convert the object into a dict
user_subscription_dict = user_subscription_instance.to_dict()
# create an instance of UserSubscription from a dict
user_subscription_from_dict = UserSubscription.from_dict(user_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


