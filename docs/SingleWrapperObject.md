# SingleWrapperObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **object** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_object import SingleWrapperObject

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperObject from a JSON string
single_wrapper_object_instance = SingleWrapperObject.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperObject.to_json())

# convert the object into a dict
single_wrapper_object_dict = single_wrapper_object_instance.to_dict()
# create an instance of SingleWrapperObject from a dict
single_wrapper_object_from_dict = SingleWrapperObject.from_dict(single_wrapper_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


