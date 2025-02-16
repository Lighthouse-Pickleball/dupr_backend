# ArrayWrapperOfClubListingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[ClubListingResponse]**](ClubListingResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_club_listing_response import ArrayWrapperOfClubListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfClubListingResponse from a JSON string
array_wrapper_of_club_listing_response_instance = ArrayWrapperOfClubListingResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfClubListingResponse.to_json())

# convert the object into a dict
array_wrapper_of_club_listing_response_dict = array_wrapper_of_club_listing_response_instance.to_dict()
# create an instance of ArrayWrapperOfClubListingResponse from a dict
array_wrapper_of_club_listing_response_from_dict = ArrayWrapperOfClubListingResponse.from_dict(array_wrapper_of_club_listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


