# ArrayWrapperOfobject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | **List[object]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_ofobject import ArrayWrapperOfobject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfobject from a JSON string
array_wrapper_ofobject_instance = ArrayWrapperOfobject.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfobject.to_json())

# convert the object into a dict
array_wrapper_ofobject_dict = array_wrapper_ofobject_instance.to_dict()
# create an instance of ArrayWrapperOfobject from a dict
array_wrapper_ofobject_from_dict = ArrayWrapperOfobject.from_dict(array_wrapper_ofobject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


