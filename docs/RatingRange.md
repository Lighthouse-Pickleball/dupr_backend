# RatingRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** |  | 
**max** | **float** |  | 

## Example

```python
from dupr_backend.models.rating_range import RatingRange

# TODO update the JSON string below
json = "{}"
# create an instance of RatingRange from a JSON string
rating_range_instance = RatingRange.from_json(json)
# print the JSON string representation of the object
print(RatingRange.to_json())

# convert the object into a dict
rating_range_dict = rating_range_instance.to_dict()
# create an instance of RatingRange from a dict
rating_range_from_dict = RatingRange.from_dict(rating_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


