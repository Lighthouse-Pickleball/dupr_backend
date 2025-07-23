# UnclaimedPlayerDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**user_id** | **int** |  | 
**age** | **int** |  | [optional] 
**gender** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.unclaimed_player_details_response import UnclaimedPlayerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnclaimedPlayerDetailsResponse from a JSON string
unclaimed_player_details_response_instance = UnclaimedPlayerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(UnclaimedPlayerDetailsResponse.to_json())

# convert the object into a dict
unclaimed_player_details_response_dict = unclaimed_player_details_response_instance.to_dict()
# create an instance of UnclaimedPlayerDetailsResponse from a dict
unclaimed_player_details_response_from_dict = UnclaimedPlayerDetailsResponse.from_dict(unclaimed_player_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


