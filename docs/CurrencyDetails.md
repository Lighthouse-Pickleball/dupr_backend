# CurrencyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | 
**currency_symbol** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**currency_rate** | **float** |  | [optional] 

## Example

```python
from dupr_backend.models.currency_details import CurrencyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDetails from a JSON string
currency_details_instance = CurrencyDetails.from_json(json)
# print the JSON string representation of the object
print(CurrencyDetails.to_json())

# convert the object into a dict
currency_details_dict = currency_details_instance.to_dict()
# create an instance of CurrencyDetails from a dict
currency_details_from_dict = CurrencyDetails.from_dict(currency_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


