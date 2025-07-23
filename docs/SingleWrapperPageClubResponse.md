# SingleWrapperPageClubResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageClubResponse**](PageClubResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_club_response import SingleWrapperPageClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageClubResponse from a JSON string
single_wrapper_page_club_response_instance = SingleWrapperPageClubResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageClubResponse.to_json())

# convert the object into a dict
single_wrapper_page_club_response_dict = single_wrapper_page_club_response_instance.to_dict()
# create an instance of SingleWrapperPageClubResponse from a dict
single_wrapper_page_club_response_from_dict = SingleWrapperPageClubResponse.from_dict(single_wrapper_page_club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


