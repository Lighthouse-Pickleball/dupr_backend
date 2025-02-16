# ClubMatchHistoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 
**filters** | [**ClubMatchFilters**](ClubMatchFilters.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**sort** | [**ClubMatchSort**](ClubMatchSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.club_match_history_request import ClubMatchHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMatchHistoryRequest from a JSON string
club_match_history_request_instance = ClubMatchHistoryRequest.from_json(json)
# print the JSON string representation of the object
print ClubMatchHistoryRequest.to_json()

# convert the object into a dict
club_match_history_request_dict = club_match_history_request_instance.to_dict()
# create an instance of ClubMatchHistoryRequest from a dict
club_match_history_request_form_dict = club_match_history_request.from_dict(club_match_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


