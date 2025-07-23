# ArrayWrapperObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | **List[object]** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_object import ArrayWrapperObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperObject from a JSON string
array_wrapper_object_instance = ArrayWrapperObject.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperObject.to_json())

# convert the object into a dict
array_wrapper_object_dict = array_wrapper_object_instance.to_dict()
# create an instance of ArrayWrapperObject from a dict
array_wrapper_object_from_dict = ArrayWrapperObject.from_dict(array_wrapper_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


