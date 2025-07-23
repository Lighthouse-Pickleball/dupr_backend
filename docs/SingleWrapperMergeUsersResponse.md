# SingleWrapperMergeUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**MergeUsersResponse**](MergeUsersResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_merge_users_response import SingleWrapperMergeUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMergeUsersResponse from a JSON string
single_wrapper_merge_users_response_instance = SingleWrapperMergeUsersResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMergeUsersResponse.to_json())

# convert the object into a dict
single_wrapper_merge_users_response_dict = single_wrapper_merge_users_response_instance.to_dict()
# create an instance of SingleWrapperMergeUsersResponse from a dict
single_wrapper_merge_users_response_from_dict = SingleWrapperMergeUsersResponse.from_dict(single_wrapper_merge_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


