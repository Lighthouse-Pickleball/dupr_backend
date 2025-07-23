# SingleWrapperString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_string import SingleWrapperString

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperString from a JSON string
single_wrapper_string_instance = SingleWrapperString.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperString.to_json())

# convert the object into a dict
single_wrapper_string_dict = single_wrapper_string_instance.to_dict()
# create an instance of SingleWrapperString from a dict
single_wrapper_string_from_dict = SingleWrapperString.from_dict(single_wrapper_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


