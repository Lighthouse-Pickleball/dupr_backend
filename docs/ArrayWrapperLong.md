# ArrayWrapperLong


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | **List[int]** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_long import ArrayWrapperLong

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperLong from a JSON string
array_wrapper_long_instance = ArrayWrapperLong.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperLong.to_json())

# convert the object into a dict
array_wrapper_long_dict = array_wrapper_long_instance.to_dict()
# create an instance of ArrayWrapperLong from a dict
array_wrapper_long_from_dict = ArrayWrapperLong.from_dict(array_wrapper_long_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


