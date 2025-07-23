# ClubListingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**club_name** | **str** |  | 
**media_url** | **str** |  | [optional] 
**short_address** | **str** |  | [optional] 
**club_member_count** | **int** |  | 
**created** | **datetime** |  | [optional] 
**role** | [**ClubRoleResponse**](ClubRoleResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.club_listing_response import ClubListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubListingResponse from a JSON string
club_listing_response_instance = ClubListingResponse.from_json(json)
# print the JSON string representation of the object
print(ClubListingResponse.to_json())

# convert the object into a dict
club_listing_response_dict = club_listing_response_instance.to_dict()
# create an instance of ClubListingResponse from a dict
club_listing_response_from_dict = ClubListingResponse.from_dict(club_listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


