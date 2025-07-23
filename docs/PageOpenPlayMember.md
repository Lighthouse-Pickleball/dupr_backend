# PageOpenPlayMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[OpenPlayMember]**](OpenPlayMember.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**has_previous** | **bool** | Is there any previous page | 
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_open_play_member import PageOpenPlayMember

# TODO update the JSON string below
json = "{}"
# create an instance of PageOpenPlayMember from a JSON string
page_open_play_member_instance = PageOpenPlayMember.from_json(json)
# print the JSON string representation of the object
print(PageOpenPlayMember.to_json())

# convert the object into a dict
page_open_play_member_dict = page_open_play_member_instance.to_dict()
# create an instance of PageOpenPlayMember from a dict
page_open_play_member_from_dict = PageOpenPlayMember.from_dict(page_open_play_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


