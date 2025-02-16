# SingleWrapperOfobject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **object** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_ofobject import SingleWrapperOfobject

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfobject from a JSON string
single_wrapper_ofobject_instance = SingleWrapperOfobject.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfobject.to_json()

# convert the object into a dict
single_wrapper_ofobject_dict = single_wrapper_ofobject_instance.to_dict()
# create an instance of SingleWrapperOfobject from a dict
single_wrapper_ofobject_form_dict = single_wrapper_ofobject.from_dict(single_wrapper_ofobject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


