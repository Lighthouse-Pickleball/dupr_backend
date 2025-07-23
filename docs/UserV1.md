# UserV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urn** | [**UserV1Urn**](UserV1Urn.md) |  | 
**user** | [**User**](User.md) |  | 

## Example

```python
from dupr_backend.models.user_v1 import UserV1

# TODO update the JSON string below
json = "{}"
# create an instance of UserV1 from a JSON string
user_v1_instance = UserV1.from_json(json)
# print the JSON string representation of the object
print(UserV1.to_json())

# convert the object into a dict
user_v1_dict = user_v1_instance.to_dict()
# create an instance of UserV1 from a dict
user_v1_from_dict = UserV1.from_dict(user_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


