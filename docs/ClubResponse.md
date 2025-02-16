# ClubResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_status** | [**AccountStatusResponse**](AccountStatusResponse.md) |  | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**attributes** | **object** |  | [optional] 
**club_id** | **int** |  | 
**club_join_type** | **str** |  | [optional] 
**club_member_count** | **int** |  | [optional] 
**club_name** | **str** |  | 
**club_type** | [**ClubTypeResponse**](ClubTypeResponse.md) |  | 
**created** | **str** |  | [optional] 
**currency_details** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**is_payment_setup** | **bool** |  | [optional] 
**long_description** | [**ContentResponse**](ContentResponse.md) |  | [optional] 
**manifest** | [**ContentResponse**](ContentResponse.md) |  | [optional] 
**media_url** | **str** |  | [optional] 
**model_type** | **str** |  | [optional] 
**model_value** | **float** |  | [optional] 
**pending_request_list** | **List[int]** |  | [optional] 
**requested_by** | **int** |  | [optional] 
**role** | [**ClubRoleResponse**](ClubRoleResponse.md) |  | [optional] 
**short_address** | **str** |  | [optional] 
**short_description** | [**ContentResponse**](ContentResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.club_response import ClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubResponse from a JSON string
club_response_instance = ClubResponse.from_json(json)
# print the JSON string representation of the object
print ClubResponse.to_json()

# convert the object into a dict
club_response_dict = club_response_instance.to_dict()
# create an instance of ClubResponse from a dict
club_response_form_dict = club_response.from_dict(club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


