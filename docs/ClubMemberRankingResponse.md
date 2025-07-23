# ClubMemberRankingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_ranking** | [**MemberRanking**](MemberRanking.md) |  | [optional] 
**member_ranking** | [**PageMemberRanking**](PageMemberRanking.md) |  | 

## Example

```python
from dupr_backend.models.club_member_ranking_response import ClubMemberRankingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMemberRankingResponse from a JSON string
club_member_ranking_response_instance = ClubMemberRankingResponse.from_json(json)
# print the JSON string representation of the object
print(ClubMemberRankingResponse.to_json())

# convert the object into a dict
club_member_ranking_response_dict = club_member_ranking_response_instance.to_dict()
# create an instance of ClubMemberRankingResponse from a dict
club_member_ranking_response_from_dict = ClubMemberRankingResponse.from_dict(club_member_ranking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


