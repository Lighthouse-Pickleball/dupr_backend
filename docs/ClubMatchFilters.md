# ClubMatchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_format** | **List[str]** |  | [optional] 
**event_date** | [**DateRange**](DateRange.md) |  | [optional] 
**event_name** | **str** |  | [optional] 
**player_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.club_match_filters import ClubMatchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMatchFilters from a JSON string
club_match_filters_instance = ClubMatchFilters.from_json(json)
# print the JSON string representation of the object
print(ClubMatchFilters.to_json())

# convert the object into a dict
club_match_filters_dict = club_match_filters_instance.to_dict()
# create an instance of ClubMatchFilters from a dict
club_match_filters_from_dict = ClubMatchFilters.from_dict(club_match_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


