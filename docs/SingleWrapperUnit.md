# SingleWrapperUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperUnit from a JSON string
single_wrapper_unit_instance = SingleWrapperUnit.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperUnit.to_json())

# convert the object into a dict
single_wrapper_unit_dict = single_wrapper_unit_instance.to_dict()
# create an instance of SingleWrapperUnit from a dict
single_wrapper_unit_from_dict = SingleWrapperUnit.from_dict(single_wrapper_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


