# CurrencyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | 
**currency_name** | **str** |  | 
**currency_symbol** | **str** |  | 
**min_limit** | **float** |  | 

## Example

```python
from dupr_backend.models.currency_details_response import CurrencyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDetailsResponse from a JSON string
currency_details_response_instance = CurrencyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(CurrencyDetailsResponse.to_json())

# convert the object into a dict
currency_details_response_dict = currency_details_response_instance.to_dict()
# create an instance of CurrencyDetailsResponse from a dict
currency_details_response_from_dict = CurrencyDetailsResponse.from_dict(currency_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


