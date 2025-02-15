# UserListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[int]** |  | 

## Example

```python
from dupr_backend.models.user_list_request import UserListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserListRequest from a JSON string
user_list_request_instance = UserListRequest.from_json(json)
# print the JSON string representation of the object
print(UserListRequest.to_json())

# convert the object into a dict
user_list_request_dict = user_list_request_instance.to_dict()
# create an instance of UserListRequest from a dict
user_list_request_from_dict = UserListRequest.from_dict(user_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


