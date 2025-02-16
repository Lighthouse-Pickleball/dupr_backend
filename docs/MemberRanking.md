# MemberRanking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**id** | **int** |  | 
**image_url** | **str** |  | [optional] 
**ranking** | **int** |  | 
**rating** | **str** |  | [optional] 
**reliability** | **int** |  | 

## Example

```python
from dupr_backend.models.member_ranking import MemberRanking

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRanking from a JSON string
member_ranking_instance = MemberRanking.from_json(json)
# print the JSON string representation of the object
print MemberRanking.to_json()

# convert the object into a dict
member_ranking_dict = member_ranking_instance.to_dict()
# create an instance of MemberRanking from a dict
member_ranking_form_dict = member_ranking.from_dict(member_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


