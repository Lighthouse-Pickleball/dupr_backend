# UserStatusUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**status** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.user_status_update_request import UserStatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatusUpdateRequest from a JSON string
user_status_update_request_instance = UserStatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UserStatusUpdateRequest.to_json())

# convert the object into a dict
user_status_update_request_dict = user_status_update_request_instance.to_dict()
# create an instance of UserStatusUpdateRequest from a dict
user_status_update_request_from_dict = UserStatusUpdateRequest.from_dict(user_status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


