# SingleWrapperMapStringObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **Dict[str, object]** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_map_string_object import SingleWrapperMapStringObject

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMapStringObject from a JSON string
single_wrapper_map_string_object_instance = SingleWrapperMapStringObject.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMapStringObject.to_json())

# convert the object into a dict
single_wrapper_map_string_object_dict = single_wrapper_map_string_object_instance.to_dict()
# create an instance of SingleWrapperMapStringObject from a dict
single_wrapper_map_string_object_from_dict = SingleWrapperMapStringObject.from_dict(single_wrapper_map_string_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


