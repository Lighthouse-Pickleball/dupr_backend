# OpenPlayMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dupr_id** | **str** |  | [optional] 
**singles** | **str** |  | [optional] 
**doubles** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**create_at** | **date** |  | [optional] 
**event_id** | **int** |  | 

## Example

```python
from dupr_backend.models.open_play_member import OpenPlayMember

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlayMember from a JSON string
open_play_member_instance = OpenPlayMember.from_json(json)
# print the JSON string representation of the object
print(OpenPlayMember.to_json())

# convert the object into a dict
open_play_member_dict = open_play_member_instance.to_dict()
# create an instance of OpenPlayMember from a dict
open_play_member_from_dict = OpenPlayMember.from_dict(open_play_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


