# ClaimPlayerSearchFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | [**AgeFilter**](AgeFilter.md) |  | [optional] 
**gender** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**radius_in_meters** | **float** |  | [optional] 
**rating** | [**ClaimPlayerRatingFilter**](ClaimPlayerRatingFilter.md) |  | [optional] 
**short_address** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.claim_player_search_filter import ClaimPlayerSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimPlayerSearchFilter from a JSON string
claim_player_search_filter_instance = ClaimPlayerSearchFilter.from_json(json)
# print the JSON string representation of the object
print ClaimPlayerSearchFilter.to_json()

# convert the object into a dict
claim_player_search_filter_dict = claim_player_search_filter_instance.to_dict()
# create an instance of ClaimPlayerSearchFilter from a dict
claim_player_search_filter_form_dict = claim_player_search_filter.from_dict(claim_player_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


