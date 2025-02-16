# ArrayWrapperOfCurrencyDetailsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[CurrencyDetailsResponse]**](CurrencyDetailsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_currency_details_response import ArrayWrapperOfCurrencyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfCurrencyDetailsResponse from a JSON string
array_wrapper_of_currency_details_response_instance = ArrayWrapperOfCurrencyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ArrayWrapperOfCurrencyDetailsResponse.to_json()

# convert the object into a dict
array_wrapper_of_currency_details_response_dict = array_wrapper_of_currency_details_response_instance.to_dict()
# create an instance of ArrayWrapperOfCurrencyDetailsResponse from a dict
array_wrapper_of_currency_details_response_form_dict = array_wrapper_of_currency_details_response.from_dict(array_wrapper_of_currency_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


