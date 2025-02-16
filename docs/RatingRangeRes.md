# RatingRangeRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** |  | 
**min** | **float** |  | 

## Example

```python
from dupr_backend.models.rating_range_res import RatingRangeRes

# TODO update the JSON string below
json = "{}"
# create an instance of RatingRangeRes from a JSON string
rating_range_res_instance = RatingRangeRes.from_json(json)
# print the JSON string representation of the object
print(RatingRangeRes.to_json())

# convert the object into a dict
rating_range_res_dict = rating_range_res_instance.to_dict()
# create an instance of RatingRangeRes from a dict
rating_range_res_from_dict = RatingRangeRes.from_dict(rating_range_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


