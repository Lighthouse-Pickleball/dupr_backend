# MergeUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**source_type** | **str** |  | 
**target** | **str** |  | 
**target_type** | **str** |  | 

## Example

```python
from dupr_backend.models.merge_users_request import MergeUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeUsersRequest from a JSON string
merge_users_request_instance = MergeUsersRequest.from_json(json)
# print the JSON string representation of the object
print(MergeUsersRequest.to_json())

# convert the object into a dict
merge_users_request_dict = merge_users_request_instance.to_dict()
# create an instance of MergeUsersRequest from a dict
merge_users_request_from_dict = MergeUsersRequest.from_dict(merge_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


