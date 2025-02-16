# ClubCurrencyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | 

## Example

```python
from dupr_backend.models.club_currency_request import ClubCurrencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClubCurrencyRequest from a JSON string
club_currency_request_instance = ClubCurrencyRequest.from_json(json)
# print the JSON string representation of the object
print ClubCurrencyRequest.to_json()

# convert the object into a dict
club_currency_request_dict = club_currency_request_instance.to_dict()
# create an instance of ClubCurrencyRequest from a dict
club_currency_request_form_dict = club_currency_request.from_dict(club_currency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


