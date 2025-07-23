# PageClubResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[ClubResponse]**](ClubResponse.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**has_previous** | **bool** | Is there any previous page | 
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_club_response import PageClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageClubResponse from a JSON string
page_club_response_instance = PageClubResponse.from_json(json)
# print the JSON string representation of the object
print(PageClubResponse.to_json())

# convert the object into a dict
page_club_response_dict = page_club_response_instance.to_dict()
# create an instance of PageClubResponse from a dict
page_club_response_from_dict = PageClubResponse.from_dict(page_club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


