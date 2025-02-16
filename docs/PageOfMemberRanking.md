# PageOfMemberRanking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 
**has_previous** | **bool** | Is there any previous page | 
**hits** | [**List[MemberRanking]**](MemberRanking.md) | Array of results, can be empty. | [optional] 
**limit** | **int** | Limit value you sent in the request | 
**offset** | **int** | Offset value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**total_value_relation** | **str** | Relation to total results available. | 

## Example

```python
from dupr_backend.models.page_of_member_ranking import PageOfMemberRanking

# TODO update the JSON string below
json = "{}"
# create an instance of PageOfMemberRanking from a JSON string
page_of_member_ranking_instance = PageOfMemberRanking.from_json(json)
# print the JSON string representation of the object
print PageOfMemberRanking.to_json()

# convert the object into a dict
page_of_member_ranking_dict = page_of_member_ranking_instance.to_dict()
# create an instance of PageOfMemberRanking from a dict
page_of_member_ranking_form_dict = page_of_member_ranking.from_dict(page_of_member_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


