# SingleWrapperPlayerRatingOvertime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PlayerRatingOvertime**](PlayerRatingOvertime.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_player_rating_overtime import SingleWrapperPlayerRatingOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPlayerRatingOvertime from a JSON string
single_wrapper_player_rating_overtime_instance = SingleWrapperPlayerRatingOvertime.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPlayerRatingOvertime.to_json())

# convert the object into a dict
single_wrapper_player_rating_overtime_dict = single_wrapper_player_rating_overtime_instance.to_dict()
# create an instance of SingleWrapperPlayerRatingOvertime from a dict
single_wrapper_player_rating_overtime_from_dict = SingleWrapperPlayerRatingOvertime.from_dict(single_wrapper_player_rating_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


