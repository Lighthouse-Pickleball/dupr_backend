# MatchRatings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_opponent_dupr** | **str** |  | [optional] 
**average_partner_dupr** | **str** |  | [optional] 
**average_points_won_percent** | **str** |  | [optional] 
**half_life** | **str** |  | [optional] 
**losses** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.match_ratings import MatchRatings

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRatings from a JSON string
match_ratings_instance = MatchRatings.from_json(json)
# print the JSON string representation of the object
print MatchRatings.to_json()

# convert the object into a dict
match_ratings_dict = match_ratings_instance.to_dict()
# create an instance of MatchRatings from a dict
match_ratings_form_dict = match_ratings.from_dict(match_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


