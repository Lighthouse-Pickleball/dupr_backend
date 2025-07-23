# SingleWrapperPagePlayerRatingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PagePlayerRatingHistory**](PagePlayerRatingHistory.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_player_rating_history import SingleWrapperPagePlayerRatingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPagePlayerRatingHistory from a JSON string
single_wrapper_page_player_rating_history_instance = SingleWrapperPagePlayerRatingHistory.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPagePlayerRatingHistory.to_json())

# convert the object into a dict
single_wrapper_page_player_rating_history_dict = single_wrapper_page_player_rating_history_instance.to_dict()
# create an instance of SingleWrapperPagePlayerRatingHistory from a dict
single_wrapper_page_player_rating_history_from_dict = SingleWrapperPagePlayerRatingHistory.from_dict(single_wrapper_page_player_rating_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


