# ArrayWrapperCurrencyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[CurrencyDetailsResponse]**](CurrencyDetailsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_currency_details_response import ArrayWrapperCurrencyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperCurrencyDetailsResponse from a JSON string
array_wrapper_currency_details_response_instance = ArrayWrapperCurrencyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperCurrencyDetailsResponse.to_json())

# convert the object into a dict
array_wrapper_currency_details_response_dict = array_wrapper_currency_details_response_instance.to_dict()
# create an instance of ArrayWrapperCurrencyDetailsResponse from a dict
array_wrapper_currency_details_response_from_dict = ArrayWrapperCurrencyDetailsResponse.from_dict(array_wrapper_currency_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


