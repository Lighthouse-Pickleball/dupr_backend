# BracketDetailsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elimination** | **str** |  | [optional] 
**event_format** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.bracket_details_response import BracketDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BracketDetailsResponse from a JSON string
bracket_details_response_instance = BracketDetailsResponse.from_json(json)
# print the JSON string representation of the object
print BracketDetailsResponse.to_json()

# convert the object into a dict
bracket_details_response_dict = bracket_details_response_instance.to_dict()
# create an instance of BracketDetailsResponse from a dict
bracket_details_response_form_dict = bracket_details_response.from_dict(bracket_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


