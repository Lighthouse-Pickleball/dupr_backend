# SingleWrapperOfCurrencyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_currency_details_response import SingleWrapperOfCurrencyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfCurrencyDetailsResponse from a JSON string
single_wrapper_of_currency_details_response_instance = SingleWrapperOfCurrencyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfCurrencyDetailsResponse.to_json())

# convert the object into a dict
single_wrapper_of_currency_details_response_dict = single_wrapper_of_currency_details_response_instance.to_dict()
# create an instance of SingleWrapperOfCurrencyDetailsResponse from a dict
single_wrapper_of_currency_details_response_from_dict = SingleWrapperOfCurrencyDetailsResponse.from_dict(single_wrapper_of_currency_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


