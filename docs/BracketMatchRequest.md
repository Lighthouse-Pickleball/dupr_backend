# BracketMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.bracket_match_request import BracketMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BracketMatchRequest from a JSON string
bracket_match_request_instance = BracketMatchRequest.from_json(json)
# print the JSON string representation of the object
print(BracketMatchRequest.to_json())

# convert the object into a dict
bracket_match_request_dict = bracket_match_request_instance.to_dict()
# create an instance of BracketMatchRequest from a dict
bracket_match_request_from_dict = BracketMatchRequest.from_dict(bracket_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


