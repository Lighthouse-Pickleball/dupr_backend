# PlayerRatingUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**new_rating** | **float** |  | [optional] 

## Example

```python
from dupr_backend.models.player_rating_update_request import PlayerRatingUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRatingUpdateRequest from a JSON string
player_rating_update_request_instance = PlayerRatingUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PlayerRatingUpdateRequest.to_json()

# convert the object into a dict
player_rating_update_request_dict = player_rating_update_request_instance.to_dict()
# create an instance of PlayerRatingUpdateRequest from a dict
player_rating_update_request_form_dict = player_rating_update_request.from_dict(player_rating_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


