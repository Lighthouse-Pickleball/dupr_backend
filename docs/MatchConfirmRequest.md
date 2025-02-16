# MatchConfirmRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** |  | 

## Example

```python
from dupr_backend.models.match_confirm_request import MatchConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchConfirmRequest from a JSON string
match_confirm_request_instance = MatchConfirmRequest.from_json(json)
# print the JSON string representation of the object
print MatchConfirmRequest.to_json()

# convert the object into a dict
match_confirm_request_dict = match_confirm_request_instance.to_dict()
# create an instance of MatchConfirmRequest from a dict
match_confirm_request_form_dict = match_confirm_request.from_dict(match_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


