# SingleWrapperOfPlayerRatingOvertime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PlayerRatingOvertime**](PlayerRatingOvertime.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_player_rating_overtime import SingleWrapperOfPlayerRatingOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPlayerRatingOvertime from a JSON string
single_wrapper_of_player_rating_overtime_instance = SingleWrapperOfPlayerRatingOvertime.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPlayerRatingOvertime.to_json())

# convert the object into a dict
single_wrapper_of_player_rating_overtime_dict = single_wrapper_of_player_rating_overtime_instance.to_dict()
# create an instance of SingleWrapperOfPlayerRatingOvertime from a dict
single_wrapper_of_player_rating_overtime_from_dict = SingleWrapperOfPlayerRatingOvertime.from_dict(single_wrapper_of_player_rating_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


