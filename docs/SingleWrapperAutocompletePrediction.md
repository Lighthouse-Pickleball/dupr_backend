# SingleWrapperAutocompletePrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**List[AutocompletePrediction]**](AutocompletePrediction.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_autocomplete_prediction import SingleWrapperAutocompletePrediction

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperAutocompletePrediction from a JSON string
single_wrapper_autocomplete_prediction_instance = SingleWrapperAutocompletePrediction.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperAutocompletePrediction.to_json())

# convert the object into a dict
single_wrapper_autocomplete_prediction_dict = single_wrapper_autocomplete_prediction_instance.to_dict()
# create an instance of SingleWrapperAutocompletePrediction from a dict
single_wrapper_autocomplete_prediction_from_dict = SingleWrapperAutocompletePrediction.from_dict(single_wrapper_autocomplete_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


