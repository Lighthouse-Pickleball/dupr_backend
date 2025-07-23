# SingleWrapperUnclaimedPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**UnclaimedPlayerResponse**](UnclaimedPlayerResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_unclaimed_player_response import SingleWrapperUnclaimedPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperUnclaimedPlayerResponse from a JSON string
single_wrapper_unclaimed_player_response_instance = SingleWrapperUnclaimedPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperUnclaimedPlayerResponse.to_json())

# convert the object into a dict
single_wrapper_unclaimed_player_response_dict = single_wrapper_unclaimed_player_response_instance.to_dict()
# create an instance of SingleWrapperUnclaimedPlayerResponse from a dict
single_wrapper_unclaimed_player_response_from_dict = SingleWrapperUnclaimedPlayerResponse.from_dict(single_wrapper_unclaimed_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


