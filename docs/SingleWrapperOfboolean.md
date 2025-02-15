# SingleWrapperOfboolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_ofboolean import SingleWrapperOfboolean

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfboolean from a JSON string
single_wrapper_ofboolean_instance = SingleWrapperOfboolean.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfboolean.to_json())

# convert the object into a dict
single_wrapper_ofboolean_dict = single_wrapper_ofboolean_instance.to_dict()
# create an instance of SingleWrapperOfboolean from a dict
single_wrapper_ofboolean_from_dict = SingleWrapperOfboolean.from_dict(single_wrapper_ofboolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


