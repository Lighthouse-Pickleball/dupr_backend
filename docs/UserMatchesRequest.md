# UserMatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**league_match_id** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from dupr_backend.models.user_matches_request import UserMatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserMatchesRequest from a JSON string
user_matches_request_instance = UserMatchesRequest.from_json(json)
# print the JSON string representation of the object
print(UserMatchesRequest.to_json())

# convert the object into a dict
user_matches_request_dict = user_matches_request_instance.to_dict()
# create an instance of UserMatchesRequest from a dict
user_matches_request_from_dict = UserMatchesRequest.from_dict(user_matches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


