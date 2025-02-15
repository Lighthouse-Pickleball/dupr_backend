# SingleWrapperOfMapOfstringAndobject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **object** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_map_ofstring_andobject import SingleWrapperOfMapOfstringAndobject

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfMapOfstringAndobject from a JSON string
single_wrapper_of_map_ofstring_andobject_instance = SingleWrapperOfMapOfstringAndobject.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfMapOfstringAndobject.to_json())

# convert the object into a dict
single_wrapper_of_map_ofstring_andobject_dict = single_wrapper_of_map_ofstring_andobject_instance.to_dict()
# create an instance of SingleWrapperOfMapOfstringAndobject from a dict
single_wrapper_of_map_ofstring_andobject_from_dict = SingleWrapperOfMapOfstringAndobject.from_dict(single_wrapper_of_map_ofstring_andobject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


