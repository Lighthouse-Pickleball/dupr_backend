# ActivityUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**profile_image** | **str** |  | 
**is_follow** | **bool** |  | 

## Example

```python
from dupr_backend.models.activity_user import ActivityUser

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityUser from a JSON string
activity_user_instance = ActivityUser.from_json(json)
# print the JSON string representation of the object
print(ActivityUser.to_json())

# convert the object into a dict
activity_user_dict = activity_user_instance.to_dict()
# create an instance of ActivityUser from a dict
activity_user_from_dict = ActivityUser.from_dict(activity_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


