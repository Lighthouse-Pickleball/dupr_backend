# MatchedSubstring


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.matched_substring import MatchedSubstring

# TODO update the JSON string below
json = "{}"
# create an instance of MatchedSubstring from a JSON string
matched_substring_instance = MatchedSubstring.from_json(json)
# print the JSON string representation of the object
print MatchedSubstring.to_json()

# convert the object into a dict
matched_substring_dict = matched_substring_instance.to_dict()
# create an instance of MatchedSubstring from a dict
matched_substring_form_dict = matched_substring.from_dict(matched_substring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


