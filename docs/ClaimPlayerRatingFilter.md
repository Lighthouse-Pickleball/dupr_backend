# ClaimPlayerRatingFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_rating** | **float** |  | 
**max_rating** | **float** |  | 
**type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.claim_player_rating_filter import ClaimPlayerRatingFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimPlayerRatingFilter from a JSON string
claim_player_rating_filter_instance = ClaimPlayerRatingFilter.from_json(json)
# print the JSON string representation of the object
print(ClaimPlayerRatingFilter.to_json())

# convert the object into a dict
claim_player_rating_filter_dict = claim_player_rating_filter_instance.to_dict()
# create an instance of ClaimPlayerRatingFilter from a dict
claim_player_rating_filter_from_dict = ClaimPlayerRatingFilter.from_dict(claim_player_rating_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


