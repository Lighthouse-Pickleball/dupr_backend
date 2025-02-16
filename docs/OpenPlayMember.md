# OpenPlayMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_at** | **str** |  | [optional] 
**doubles** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**event_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**singles** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.open_play_member import OpenPlayMember

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlayMember from a JSON string
open_play_member_instance = OpenPlayMember.from_json(json)
# print the JSON string representation of the object
print OpenPlayMember.to_json()

# convert the object into a dict
open_play_member_dict = open_play_member_instance.to_dict()
# create an instance of OpenPlayMember from a dict
open_play_member_form_dict = open_play_member.from_dict(open_play_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


