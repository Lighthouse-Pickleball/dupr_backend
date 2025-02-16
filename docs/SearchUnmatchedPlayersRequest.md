# SearchUnmatchedPlayersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**query** | **str** |  | [optional] 
**sort** | [**BracketUnmatchedPlayerSort**](BracketUnmatchedPlayerSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.search_unmatched_players_request import SearchUnmatchedPlayersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUnmatchedPlayersRequest from a JSON string
search_unmatched_players_request_instance = SearchUnmatchedPlayersRequest.from_json(json)
# print the JSON string representation of the object
print SearchUnmatchedPlayersRequest.to_json()

# convert the object into a dict
search_unmatched_players_request_dict = search_unmatched_players_request_instance.to_dict()
# create an instance of SearchUnmatchedPlayersRequest from a dict
search_unmatched_players_request_form_dict = search_unmatched_players_request.from_dict(search_unmatched_players_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


