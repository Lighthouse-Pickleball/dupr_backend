# SingleWrapperClubResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**ClubResponse**](ClubResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_club_response import SingleWrapperClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperClubResponse from a JSON string
single_wrapper_club_response_instance = SingleWrapperClubResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperClubResponse.to_json())

# convert the object into a dict
single_wrapper_club_response_dict = single_wrapper_club_response_instance.to_dict()
# create an instance of SingleWrapperClubResponse from a dict
single_wrapper_club_response_from_dict = SingleWrapperClubResponse.from_dict(single_wrapper_club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


