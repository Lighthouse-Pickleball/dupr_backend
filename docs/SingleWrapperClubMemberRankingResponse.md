# SingleWrapperClubMemberRankingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**ClubMemberRankingResponse**](ClubMemberRankingResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_club_member_ranking_response import SingleWrapperClubMemberRankingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperClubMemberRankingResponse from a JSON string
single_wrapper_club_member_ranking_response_instance = SingleWrapperClubMemberRankingResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperClubMemberRankingResponse.to_json())

# convert the object into a dict
single_wrapper_club_member_ranking_response_dict = single_wrapper_club_member_ranking_response_instance.to_dict()
# create an instance of SingleWrapperClubMemberRankingResponse from a dict
single_wrapper_club_member_ranking_response_from_dict = SingleWrapperClubMemberRankingResponse.from_dict(single_wrapper_club_member_ranking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


