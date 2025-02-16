# SearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 
**exclude_club_members** | [**ExcludeClubMembers**](ExcludeClubMembers.md) |  | [optional] 
**filter** | [**SearchFilter**](SearchFilter.md) |  | 
**include_unclaimed_players** | **bool** |  | [optional] 
**limit** | **int** |  | 
**offset** | **int** |  | 
**page_source** | **str** |  | [optional] 
**query** | **str** |  | 
**verified_email** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print SearchRequest.to_json()

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_form_dict = search_request.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


