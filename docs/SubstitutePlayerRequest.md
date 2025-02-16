# SubstitutePlayerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**is_club_member** | **bool** |  | 
**league_match_id** | **int** |  | 
**player_id** | **int** |  | 
**sub_player_id** | **int** |  | 

## Example

```python
from dupr_backend.models.substitute_player_request import SubstitutePlayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubstitutePlayerRequest from a JSON string
substitute_player_request_instance = SubstitutePlayerRequest.from_json(json)
# print the JSON string representation of the object
print SubstitutePlayerRequest.to_json()

# convert the object into a dict
substitute_player_request_dict = substitute_player_request_instance.to_dict()
# create an instance of SubstitutePlayerRequest from a dict
substitute_player_request_form_dict = substitute_player_request.from_dict(substitute_player_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


