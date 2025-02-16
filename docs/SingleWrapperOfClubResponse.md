# SingleWrapperOfClubResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**ClubResponse**](ClubResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_club_response import SingleWrapperOfClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfClubResponse from a JSON string
single_wrapper_of_club_response_instance = SingleWrapperOfClubResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfClubResponse.to_json()

# convert the object into a dict
single_wrapper_of_club_response_dict = single_wrapper_of_club_response_instance.to_dict()
# create an instance of SingleWrapperOfClubResponse from a dict
single_wrapper_of_club_response_form_dict = single_wrapper_of_club_response.from_dict(single_wrapper_of_club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


