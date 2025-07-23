# ResultUnclaimedPlayerDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | [**List[UnclaimedPlayerDetailsResponse]**](UnclaimedPlayerDetailsResponse.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_unclaimed_player_details_response import ResultUnclaimedPlayerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultUnclaimedPlayerDetailsResponse from a JSON string
result_unclaimed_player_details_response_instance = ResultUnclaimedPlayerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ResultUnclaimedPlayerDetailsResponse.to_json())

# convert the object into a dict
result_unclaimed_player_details_response_dict = result_unclaimed_player_details_response_instance.to_dict()
# create an instance of ResultUnclaimedPlayerDetailsResponse from a dict
result_unclaimed_player_details_response_from_dict = ResultUnclaimedPlayerDetailsResponse.from_dict(result_unclaimed_player_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


