# PageClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[ClubMemberResponse]**](ClubMemberResponse.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**empty** | **bool** | Are results empty | 
**has_previous** | **bool** | Is there any previous page | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_club_member_response import PageClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageClubMemberResponse from a JSON string
page_club_member_response_instance = PageClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print(PageClubMemberResponse.to_json())

# convert the object into a dict
page_club_member_response_dict = page_club_member_response_instance.to_dict()
# create an instance of PageClubMemberResponse from a dict
page_club_member_response_from_dict = PageClubMemberResponse.from_dict(page_club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


