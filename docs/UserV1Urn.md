# UserV1Urn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**type** | **str** |  | 
**version** | **str** |  | 
**id** | **str** |  | 
**nid** | **str** |  | 

## Example

```python
from dupr_backend.models.user_v1_urn import UserV1Urn

# TODO update the JSON string below
json = "{}"
# create an instance of UserV1Urn from a JSON string
user_v1_urn_instance = UserV1Urn.from_json(json)
# print the JSON string representation of the object
print(UserV1Urn.to_json())

# convert the object into a dict
user_v1_urn_dict = user_v1_urn_instance.to_dict()
# create an instance of UserV1Urn from a dict
user_v1_urn_from_dict = UserV1Urn.from_dict(user_v1_urn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


