# MatchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_format** | **List[str]** |  | [optional] 
**match_status** | **List[str]** |  | [optional] 
**event_date** | [**DateRange**](DateRange.md) |  | [optional] 
**event_name** | **str** |  | [optional] 
**player_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.match_filters import MatchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFilters from a JSON string
match_filters_instance = MatchFilters.from_json(json)
# print the JSON string representation of the object
print(MatchFilters.to_json())

# convert the object into a dict
match_filters_dict = match_filters_instance.to_dict()
# create an instance of MatchFilters from a dict
match_filters_from_dict = MatchFilters.from_dict(match_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


