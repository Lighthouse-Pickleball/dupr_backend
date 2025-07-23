# Club


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**club_name** | **str** |  | 
**club_code** | **str** |  | 
**club_type** | [**ClubType**](ClubType.md) |  | [optional] 
**media_url** | **str** |  | [optional] 
**manifest** | [**TextContent**](TextContent.md) |  | [optional] 
**short_description** | [**TextContent**](TextContent.md) |  | [optional] 
**long_description** | [**TextContent**](TextContent.md) |  | [optional] 
**approval_status** | **str** |  | 
**status** | **str** |  | 
**attributes** | **object** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**short_address** | **str** |  | [optional] 
**revenue_model** | [**RevenueModel**](RevenueModel.md) |  | [optional] 
**currency_details** | [**CurrencyDetails**](CurrencyDetails.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**club_join_type** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | 

## Example

```python
from dupr_backend.models.club import Club

# TODO update the JSON string below
json = "{}"
# create an instance of Club from a JSON string
club_instance = Club.from_json(json)
# print the JSON string representation of the object
print(Club.to_json())

# convert the object into a dict
club_dict = club_instance.to_dict()
# create an instance of Club from a dict
club_from_dict = Club.from_dict(club_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


