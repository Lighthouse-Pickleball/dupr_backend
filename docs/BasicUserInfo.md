# BasicUserInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**referral_code** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.basic_user_info import BasicUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BasicUserInfo from a JSON string
basic_user_info_instance = BasicUserInfo.from_json(json)
# print the JSON string representation of the object
print BasicUserInfo.to_json()

# convert the object into a dict
basic_user_info_dict = basic_user_info_instance.to_dict()
# create an instance of BasicUserInfo from a dict
basic_user_info_form_dict = basic_user_info.from_dict(basic_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


