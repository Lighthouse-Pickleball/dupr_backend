# FollowingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_followed** | **bool** |  | 
**followers** | **int** |  | 
**followings** | **int** |  | 

## Example

```python
from dupr_backend.models.following_info import FollowingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FollowingInfo from a JSON string
following_info_instance = FollowingInfo.from_json(json)
# print the JSON string representation of the object
print(FollowingInfo.to_json())

# convert the object into a dict
following_info_dict = following_info_instance.to_dict()
# create an instance of FollowingInfo from a dict
following_info_from_dict = FollowingInfo.from_dict(following_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


