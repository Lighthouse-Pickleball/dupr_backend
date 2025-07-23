# SingleWrapperBoolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_boolean import SingleWrapperBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperBoolean from a JSON string
single_wrapper_boolean_instance = SingleWrapperBoolean.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperBoolean.to_json())

# convert the object into a dict
single_wrapper_boolean_dict = single_wrapper_boolean_instance.to_dict()
# create an instance of SingleWrapperBoolean from a dict
single_wrapper_boolean_from_dict = SingleWrapperBoolean.from_dict(single_wrapper_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


