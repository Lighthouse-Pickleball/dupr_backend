# SingleWrapperOflong


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_oflong import SingleWrapperOflong

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOflong from a JSON string
single_wrapper_oflong_instance = SingleWrapperOflong.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOflong.to_json())

# convert the object into a dict
single_wrapper_oflong_dict = single_wrapper_oflong_instance.to_dict()
# create an instance of SingleWrapperOflong from a dict
single_wrapper_oflong_from_dict = SingleWrapperOflong.from_dict(single_wrapper_oflong_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


