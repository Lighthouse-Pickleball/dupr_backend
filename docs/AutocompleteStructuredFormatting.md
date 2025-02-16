# AutocompleteStructuredFormatting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_text** | **str** |  | [optional] 
**main_text_matched_substrings** | [**List[MatchedSubstring]**](MatchedSubstring.md) |  | [optional] 
**secondary_text** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.autocomplete_structured_formatting import AutocompleteStructuredFormatting

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteStructuredFormatting from a JSON string
autocomplete_structured_formatting_instance = AutocompleteStructuredFormatting.from_json(json)
# print the JSON string representation of the object
print AutocompleteStructuredFormatting.to_json()

# convert the object into a dict
autocomplete_structured_formatting_dict = autocomplete_structured_formatting_instance.to_dict()
# create an instance of AutocompleteStructuredFormatting from a dict
autocomplete_structured_formatting_form_dict = autocomplete_structured_formatting.from_dict(autocomplete_structured_formatting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


