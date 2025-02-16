# AutocompletePrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**distance_meters** | **int** |  | [optional] 
**matched_substrings** | [**List[MatchedSubstring]**](MatchedSubstring.md) |  | [optional] 
**place_id** | **str** |  | [optional] 
**structured_formatting** | [**AutocompleteStructuredFormatting**](AutocompleteStructuredFormatting.md) |  | [optional] 
**terms** | [**List[Term]**](Term.md) |  | [optional] 
**types** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.autocomplete_prediction import AutocompletePrediction

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompletePrediction from a JSON string
autocomplete_prediction_instance = AutocompletePrediction.from_json(json)
# print the JSON string representation of the object
print(AutocompletePrediction.to_json())

# convert the object into a dict
autocomplete_prediction_dict = autocomplete_prediction_instance.to_dict()
# create an instance of AutocompletePrediction from a dict
autocomplete_prediction_from_dict = AutocompletePrediction.from_dict(autocomplete_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


