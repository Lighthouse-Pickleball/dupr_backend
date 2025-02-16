# ArrayWrapperOfActivityUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[ActivityUser]**](ActivityUser.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_activity_user import ArrayWrapperOfActivityUser

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfActivityUser from a JSON string
array_wrapper_of_activity_user_instance = ArrayWrapperOfActivityUser.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfActivityUser.to_json())

# convert the object into a dict
array_wrapper_of_activity_user_dict = array_wrapper_of_activity_user_instance.to_dict()
# create an instance of ArrayWrapperOfActivityUser from a dict
array_wrapper_of_activity_user_from_dict = ArrayWrapperOfActivityUser.from_dict(array_wrapper_of_activity_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


