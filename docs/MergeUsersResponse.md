# MergeUsersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**target** | **str** |  | 

## Example

```python
from dupr_backend.models.merge_users_response import MergeUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MergeUsersResponse from a JSON string
merge_users_response_instance = MergeUsersResponse.from_json(json)
# print the JSON string representation of the object
print MergeUsersResponse.to_json()

# convert the object into a dict
merge_users_response_dict = merge_users_response_instance.to_dict()
# create an instance of MergeUsersResponse from a dict
merge_users_response_form_dict = merge_users_response.from_dict(merge_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


