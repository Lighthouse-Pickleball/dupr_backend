# SingleWrapperCurrencyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_currency_details_response import SingleWrapperCurrencyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperCurrencyDetailsResponse from a JSON string
single_wrapper_currency_details_response_instance = SingleWrapperCurrencyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperCurrencyDetailsResponse.to_json())

# convert the object into a dict
single_wrapper_currency_details_response_dict = single_wrapper_currency_details_response_instance.to_dict()
# create an instance of SingleWrapperCurrencyDetailsResponse from a dict
single_wrapper_currency_details_response_from_dict = SingleWrapperCurrencyDetailsResponse.from_dict(single_wrapper_currency_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


