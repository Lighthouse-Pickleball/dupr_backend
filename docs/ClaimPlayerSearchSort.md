# ClaimPlayerSearchSort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** |  | [optional] 
**parameter** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.claim_player_search_sort import ClaimPlayerSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimPlayerSearchSort from a JSON string
claim_player_search_sort_instance = ClaimPlayerSearchSort.from_json(json)
# print the JSON string representation of the object
print ClaimPlayerSearchSort.to_json()

# convert the object into a dict
claim_player_search_sort_dict = claim_player_search_sort_instance.to_dict()
# create an instance of ClaimPlayerSearchSort from a dict
claim_player_search_sort_form_dict = claim_player_search_sort.from_dict(claim_player_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


