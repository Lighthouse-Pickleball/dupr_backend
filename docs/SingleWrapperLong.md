# SingleWrapperLong


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_long import SingleWrapperLong

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperLong from a JSON string
single_wrapper_long_instance = SingleWrapperLong.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperLong.to_json())

# convert the object into a dict
single_wrapper_long_dict = single_wrapper_long_instance.to_dict()
# create an instance of SingleWrapperLong from a dict
single_wrapper_long_from_dict = SingleWrapperLong.from_dict(single_wrapper_long_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


