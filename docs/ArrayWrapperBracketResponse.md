# ArrayWrapperBracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[BracketResponse]**](BracketResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_bracket_response import ArrayWrapperBracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperBracketResponse from a JSON string
array_wrapper_bracket_response_instance = ArrayWrapperBracketResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperBracketResponse.to_json())

# convert the object into a dict
array_wrapper_bracket_response_dict = array_wrapper_bracket_response_instance.to_dict()
# create an instance of ArrayWrapperBracketResponse from a dict
array_wrapper_bracket_response_from_dict = ArrayWrapperBracketResponse.from_dict(array_wrapper_bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


