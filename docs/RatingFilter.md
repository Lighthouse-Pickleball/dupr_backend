# RatingFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**max_rating** | **float** |  | [optional] 
**min_rating** | **float** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.rating_filter import RatingFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RatingFilter from a JSON string
rating_filter_instance = RatingFilter.from_json(json)
# print the JSON string representation of the object
print RatingFilter.to_json()

# convert the object into a dict
rating_filter_dict = rating_filter_instance.to_dict()
# create an instance of RatingFilter from a dict
rating_filter_form_dict = rating_filter.from_dict(rating_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


