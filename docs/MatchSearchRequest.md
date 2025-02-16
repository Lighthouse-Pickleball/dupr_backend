# MatchSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**MatchFilters**](MatchFilters.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**sort** | [**MatchSort**](MatchSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.match_search_request import MatchSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchSearchRequest from a JSON string
match_search_request_instance = MatchSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MatchSearchRequest.to_json())

# convert the object into a dict
match_search_request_dict = match_search_request_instance.to_dict()
# create an instance of MatchSearchRequest from a dict
match_search_request_from_dict = MatchSearchRequest.from_dict(match_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


