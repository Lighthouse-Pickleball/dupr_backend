# ArrayWrapperClubListingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[ClubListingResponse]**](ClubListingResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_club_listing_response import ArrayWrapperClubListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperClubListingResponse from a JSON string
array_wrapper_club_listing_response_instance = ArrayWrapperClubListingResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperClubListingResponse.to_json())

# convert the object into a dict
array_wrapper_club_listing_response_dict = array_wrapper_club_listing_response_instance.to_dict()
# create an instance of ArrayWrapperClubListingResponse from a dict
array_wrapper_club_listing_response_from_dict = ArrayWrapperClubListingResponse.from_dict(array_wrapper_club_listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


