# SingleWrapperPageOpenPlayMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageOpenPlayMember**](PageOpenPlayMember.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_open_play_member import SingleWrapperPageOpenPlayMember

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageOpenPlayMember from a JSON string
single_wrapper_page_open_play_member_instance = SingleWrapperPageOpenPlayMember.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageOpenPlayMember.to_json())

# convert the object into a dict
single_wrapper_page_open_play_member_dict = single_wrapper_page_open_play_member_instance.to_dict()
# create an instance of SingleWrapperPageOpenPlayMember from a dict
single_wrapper_page_open_play_member_from_dict = SingleWrapperPageOpenPlayMember.from_dict(single_wrapper_page_open_play_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


