# ClubSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**location** | [**ExternalFilterLocation**](ExternalFilterLocation.md) |  | [optional] 
**offset** | **int** |  | 
**own** | **bool** |  | 
**query** | **str** |  | 

## Example

```python
from dupr_backend.models.club_search import ClubSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ClubSearch from a JSON string
club_search_instance = ClubSearch.from_json(json)
# print the JSON string representation of the object
print(ClubSearch.to_json())

# convert the object into a dict
club_search_dict = club_search_instance.to_dict()
# create an instance of ClubSearch from a dict
club_search_from_dict = ClubSearch.from_dict(club_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


