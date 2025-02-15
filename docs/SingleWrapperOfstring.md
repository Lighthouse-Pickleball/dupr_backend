# SingleWrapperOfstring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_ofstring import SingleWrapperOfstring

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfstring from a JSON string
single_wrapper_ofstring_instance = SingleWrapperOfstring.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfstring.to_json())

# convert the object into a dict
single_wrapper_ofstring_dict = single_wrapper_ofstring_instance.to_dict()
# create an instance of SingleWrapperOfstring from a dict
single_wrapper_ofstring_from_dict = SingleWrapperOfstring.from_dict(single_wrapper_ofstring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


