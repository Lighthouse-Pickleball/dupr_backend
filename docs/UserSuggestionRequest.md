# UserSuggestionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_ids** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.user_suggestion_request import UserSuggestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSuggestionRequest from a JSON string
user_suggestion_request_instance = UserSuggestionRequest.from_json(json)
# print the JSON string representation of the object
print UserSuggestionRequest.to_json()

# convert the object into a dict
user_suggestion_request_dict = user_suggestion_request_instance.to_dict()
# create an instance of UserSuggestionRequest from a dict
user_suggestion_request_form_dict = user_suggestion_request.from_dict(user_suggestion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


