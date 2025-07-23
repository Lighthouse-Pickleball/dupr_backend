# ClubResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**club_name** | **str** |  | 
**club_type** | [**ClubTypeResponse**](ClubTypeResponse.md) |  | 
**media_url** | **str** |  | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**short_address** | **str** |  | [optional] 
**club_member_count** | **int** |  | 
**manifest** | [**ContentResponse**](ContentResponse.md) |  | [optional] 
**short_description** | [**ContentResponse**](ContentResponse.md) |  | [optional] 
**long_description** | [**ContentResponse**](ContentResponse.md) |  | [optional] 
**attributes** | **object** |  | [optional] 
**role** | [**ClubRoleResponse**](ClubRoleResponse.md) |  | [optional] 
**is_payment_setup** | **bool** |  | [optional] 
**account_status** | [**AccountStatusResponse**](AccountStatusResponse.md) |  | [optional] 
**model_type** | **str** |  | [optional] 
**model_value** | **float** |  | [optional] 
**currency_details** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**requested_by** | **int** |  | [optional] 
**club_join_type** | **str** |  | [optional] 
**pending_request_list** | **List[int]** |  | [optional] 
**distance_in_miles** | **float** |  | 

## Example

```python
from dupr_backend.models.club_response import ClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubResponse from a JSON string
club_response_instance = ClubResponse.from_json(json)
# print the JSON string representation of the object
print(ClubResponse.to_json())

# convert the object into a dict
club_response_dict = club_response_instance.to_dict()
# create an instance of ClubResponse from a dict
club_response_from_dict = ClubResponse.from_dict(club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


