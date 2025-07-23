# UnclaimedPlayerDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_id** | **str** |  | 

## Example

```python
from dupr_backend.models.unclaimed_player_details_request import UnclaimedPlayerDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnclaimedPlayerDetailsRequest from a JSON string
unclaimed_player_details_request_instance = UnclaimedPlayerDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(UnclaimedPlayerDetailsRequest.to_json())

# convert the object into a dict
unclaimed_player_details_request_dict = unclaimed_player_details_request_instance.to_dict()
# create an instance of UnclaimedPlayerDetailsRequest from a dict
unclaimed_player_details_request_from_dict = UnclaimedPlayerDetailsRequest.from_dict(unclaimed_player_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


