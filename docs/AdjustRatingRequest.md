# AdjustRatingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**singles** | **float** |  | [optional] 
**singles_verified** | **float** |  | [optional] 
**doubles** | **float** |  | [optional] 
**doubles_verified** | **float** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from dupr_backend.models.adjust_rating_request import AdjustRatingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustRatingRequest from a JSON string
adjust_rating_request_instance = AdjustRatingRequest.from_json(json)
# print the JSON string representation of the object
print(AdjustRatingRequest.to_json())

# convert the object into a dict
adjust_rating_request_dict = adjust_rating_request_instance.to_dict()
# create an instance of AdjustRatingRequest from a dict
adjust_rating_request_from_dict = AdjustRatingRequest.from_dict(adjust_rating_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


