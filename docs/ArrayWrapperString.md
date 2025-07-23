# ArrayWrapperString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_string import ArrayWrapperString

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperString from a JSON string
array_wrapper_string_instance = ArrayWrapperString.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperString.to_json())

# convert the object into a dict
array_wrapper_string_dict = array_wrapper_string_instance.to_dict()
# create an instance of ArrayWrapperString from a dict
array_wrapper_string_from_dict = ArrayWrapperString.from_dict(array_wrapper_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


