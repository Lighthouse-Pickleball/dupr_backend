# Wrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.wrapper import Wrapper

# TODO update the JSON string below
json = "{}"
# create an instance of Wrapper from a JSON string
wrapper_instance = Wrapper.from_json(json)
# print the JSON string representation of the object
print(Wrapper.to_json())

# convert the object into a dict
wrapper_dict = wrapper_instance.to_dict()
# create an instance of Wrapper from a dict
wrapper_from_dict = Wrapper.from_dict(wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


