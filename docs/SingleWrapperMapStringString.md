# SingleWrapperMapStringString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_map_string_string import SingleWrapperMapStringString

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMapStringString from a JSON string
single_wrapper_map_string_string_instance = SingleWrapperMapStringString.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMapStringString.to_json())

# convert the object into a dict
single_wrapper_map_string_string_dict = single_wrapper_map_string_string_instance.to_dict()
# create an instance of SingleWrapperMapStringString from a dict
single_wrapper_map_string_string_from_dict = SingleWrapperMapStringString.from_dict(single_wrapper_map_string_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


