# PageMiLPEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[MiLPEvent]**](MiLPEvent.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**has_previous** | **bool** | Is there any previous page | 
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_mi_lp_event import PageMiLPEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PageMiLPEvent from a JSON string
page_mi_lp_event_instance = PageMiLPEvent.from_json(json)
# print the JSON string representation of the object
print(PageMiLPEvent.to_json())

# convert the object into a dict
page_mi_lp_event_dict = page_mi_lp_event_instance.to_dict()
# create an instance of PageMiLPEvent from a dict
page_mi_lp_event_from_dict = PageMiLPEvent.from_dict(page_mi_lp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


