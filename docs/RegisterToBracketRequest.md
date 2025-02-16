# RegisterToBracketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**users** | [**List[RegisterUserRequest]**](RegisterUserRequest.md) |  | [optional] 

## Example

```python
from dupr_backend.models.register_to_bracket_request import RegisterToBracketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterToBracketRequest from a JSON string
register_to_bracket_request_instance = RegisterToBracketRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterToBracketRequest.to_json())

# convert the object into a dict
register_to_bracket_request_dict = register_to_bracket_request_instance.to_dict()
# create an instance of RegisterToBracketRequest from a dict
register_to_bracket_request_from_dict = RegisterToBracketRequest.from_dict(register_to_bracket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


