# SingleWrapperFollowingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**FollowingInfo**](FollowingInfo.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_following_info import SingleWrapperFollowingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperFollowingInfo from a JSON string
single_wrapper_following_info_instance = SingleWrapperFollowingInfo.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperFollowingInfo.to_json())

# convert the object into a dict
single_wrapper_following_info_dict = single_wrapper_following_info_instance.to_dict()
# create an instance of SingleWrapperFollowingInfo from a dict
single_wrapper_following_info_from_dict = SingleWrapperFollowingInfo.from_dict(single_wrapper_following_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


