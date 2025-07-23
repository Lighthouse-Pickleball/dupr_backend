# AgeRangeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_age** | **int** |  | 
**max_age** | **int** |  | 

## Example

```python
from dupr_backend.models.age_range_filter import AgeRangeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AgeRangeFilter from a JSON string
age_range_filter_instance = AgeRangeFilter.from_json(json)
# print the JSON string representation of the object
print(AgeRangeFilter.to_json())

# convert the object into a dict
age_range_filter_dict = age_range_filter_instance.to_dict()
# create an instance of AgeRangeFilter from a dict
age_range_filter_from_dict = AgeRangeFilter.from_dict(age_range_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


