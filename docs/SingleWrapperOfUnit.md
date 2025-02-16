# SingleWrapperOfUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **object** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfUnit from a JSON string
single_wrapper_of_unit_instance = SingleWrapperOfUnit.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfUnit.to_json())

# convert the object into a dict
single_wrapper_of_unit_dict = single_wrapper_of_unit_instance.to_dict()
# create an instance of SingleWrapperOfUnit from a dict
single_wrapper_of_unit_from_dict = SingleWrapperOfUnit.from_dict(single_wrapper_of_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


