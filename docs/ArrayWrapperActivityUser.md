# ArrayWrapperActivityUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[ActivityUser]**](ActivityUser.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_activity_user import ArrayWrapperActivityUser

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperActivityUser from a JSON string
array_wrapper_activity_user_instance = ArrayWrapperActivityUser.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperActivityUser.to_json())

# convert the object into a dict
array_wrapper_activity_user_dict = array_wrapper_activity_user_instance.to_dict()
# create an instance of ArrayWrapperActivityUser from a dict
array_wrapper_activity_user_from_dict = ArrayWrapperActivityUser.from_dict(array_wrapper_activity_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


