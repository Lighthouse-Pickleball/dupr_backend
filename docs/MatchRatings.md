# MatchRatings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_partner_dupr** | **float** |  | 
**average_opponent_dupr** | **float** |  | 
**average_points_won_percent** | **float** |  | 
**half_life** | **float** |  | 

## Example

```python
from dupr_backend.models.match_ratings import MatchRatings

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRatings from a JSON string
match_ratings_instance = MatchRatings.from_json(json)
# print the JSON string representation of the object
print(MatchRatings.to_json())

# convert the object into a dict
match_ratings_dict = match_ratings_instance.to_dict()
# create an instance of MatchRatings from a dict
match_ratings_from_dict = MatchRatings.from_dict(match_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


