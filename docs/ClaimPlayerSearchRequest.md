# ClaimPlayerSearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ClaimPlayerSearchFilter**](ClaimPlayerSearchFilter.md) |  | [optional] 
**limit** | **int** |  | 
**offset** | **int** |  | 
**query** | **str** |  | 
**sort** | [**ClaimPlayerSearchSort**](ClaimPlayerSearchSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.claim_player_search_request import ClaimPlayerSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimPlayerSearchRequest from a JSON string
claim_player_search_request_instance = ClaimPlayerSearchRequest.from_json(json)
# print the JSON string representation of the object
print ClaimPlayerSearchRequest.to_json()

# convert the object into a dict
claim_player_search_request_dict = claim_player_search_request_instance.to_dict()
# create an instance of ClaimPlayerSearchRequest from a dict
claim_player_search_request_form_dict = claim_player_search_request.from_dict(claim_player_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


