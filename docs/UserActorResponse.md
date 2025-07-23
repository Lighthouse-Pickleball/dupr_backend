# UserActorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_v1** | [**UserV1**](UserV1.md) |  | 

## Example

```python
from dupr_backend.models.user_actor_response import UserActorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserActorResponse from a JSON string
user_actor_response_instance = UserActorResponse.from_json(json)
# print the JSON string representation of the object
print(UserActorResponse.to_json())

# convert the object into a dict
user_actor_response_dict = user_actor_response_instance.to_dict()
# create an instance of UserActorResponse from a dict
user_actor_response_from_dict = UserActorResponse.from_dict(user_actor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


