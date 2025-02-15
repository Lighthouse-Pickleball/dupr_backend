# SingleWrapperOfArrayOfAutocompletePrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**List[AutocompletePrediction]**](AutocompletePrediction.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_array_of_autocomplete_prediction import SingleWrapperOfArrayOfAutocompletePrediction

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfArrayOfAutocompletePrediction from a JSON string
single_wrapper_of_array_of_autocomplete_prediction_instance = SingleWrapperOfArrayOfAutocompletePrediction.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfArrayOfAutocompletePrediction.to_json())

# convert the object into a dict
single_wrapper_of_array_of_autocomplete_prediction_dict = single_wrapper_of_array_of_autocomplete_prediction_instance.to_dict()
# create an instance of SingleWrapperOfArrayOfAutocompletePrediction from a dict
single_wrapper_of_array_of_autocomplete_prediction_from_dict = SingleWrapperOfArrayOfAutocompletePrediction.from_dict(single_wrapper_of_array_of_autocomplete_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


