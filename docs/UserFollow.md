# UserFollow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from dupr_backend.models.user_follow import UserFollow

# TODO update the JSON string below
json = "{}"
# create an instance of UserFollow from a JSON string
user_follow_instance = UserFollow.from_json(json)
# print the JSON string representation of the object
print(UserFollow.to_json())

# convert the object into a dict
user_follow_dict = user_follow_instance.to_dict()
# create an instance of UserFollow from a dict
user_follow_from_dict = UserFollow.from_dict(user_follow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


