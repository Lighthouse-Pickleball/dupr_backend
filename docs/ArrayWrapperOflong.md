# ArrayWrapperOflong


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | **List[int]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_oflong import ArrayWrapperOflong

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOflong from a JSON string
array_wrapper_oflong_instance = ArrayWrapperOflong.from_json(json)
# print the JSON string representation of the object
print ArrayWrapperOflong.to_json()

# convert the object into a dict
array_wrapper_oflong_dict = array_wrapper_oflong_instance.to_dict()
# create an instance of ArrayWrapperOflong from a dict
array_wrapper_oflong_form_dict = array_wrapper_oflong.from_dict(array_wrapper_oflong_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


