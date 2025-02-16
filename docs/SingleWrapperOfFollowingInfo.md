# SingleWrapperOfFollowingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**FollowingInfo**](FollowingInfo.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_following_info import SingleWrapperOfFollowingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfFollowingInfo from a JSON string
single_wrapper_of_following_info_instance = SingleWrapperOfFollowingInfo.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfFollowingInfo.to_json()

# convert the object into a dict
single_wrapper_of_following_info_dict = single_wrapper_of_following_info_instance.to_dict()
# create an instance of SingleWrapperOfFollowingInfo from a dict
single_wrapper_of_following_info_form_dict = single_wrapper_of_following_info.from_dict(single_wrapper_of_following_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


