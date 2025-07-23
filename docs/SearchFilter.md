# SearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | [**RatingFilter**](RatingFilter.md) |  | [optional] 
**gender** | **str** |  | [optional] 
**lat** | **float** |  | 
**lng** | **float** |  | 
**radius_in_meters** | **float** |  | 
**age_range** | [**AgeRangeFilter**](AgeRangeFilter.md) |  | [optional] 

## Example

```python
from dupr_backend.models.search_filter import SearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilter from a JSON string
search_filter_instance = SearchFilter.from_json(json)
# print the JSON string representation of the object
print(SearchFilter.to_json())

# convert the object into a dict
search_filter_dict = search_filter_instance.to_dict()
# create an instance of SearchFilter from a dict
search_filter_from_dict = SearchFilter.from_dict(search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


