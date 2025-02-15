# SingleWrapperOfMergeUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**MergeUsersResponse**](MergeUsersResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_merge_users_response import SingleWrapperOfMergeUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfMergeUsersResponse from a JSON string
single_wrapper_of_merge_users_response_instance = SingleWrapperOfMergeUsersResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfMergeUsersResponse.to_json())

# convert the object into a dict
single_wrapper_of_merge_users_response_dict = single_wrapper_of_merge_users_response_instance.to_dict()
# create an instance of SingleWrapperOfMergeUsersResponse from a dict
single_wrapper_of_merge_users_response_from_dict = SingleWrapperOfMergeUsersResponse.from_dict(single_wrapper_of_merge_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


