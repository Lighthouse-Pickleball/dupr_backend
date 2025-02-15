# SingleWrapperOfPageOfPlayerRatingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfPlayerRatingHistory**](PageOfPlayerRatingHistory.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_player_rating_history import SingleWrapperOfPageOfPlayerRatingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfPlayerRatingHistory from a JSON string
single_wrapper_of_page_of_player_rating_history_instance = SingleWrapperOfPageOfPlayerRatingHistory.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfPlayerRatingHistory.to_json())

# convert the object into a dict
single_wrapper_of_page_of_player_rating_history_dict = single_wrapper_of_page_of_player_rating_history_instance.to_dict()
# create an instance of SingleWrapperOfPageOfPlayerRatingHistory from a dict
single_wrapper_of_page_of_player_rating_history_from_dict = SingleWrapperOfPageOfPlayerRatingHistory.from_dict(single_wrapper_of_page_of_player_rating_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


