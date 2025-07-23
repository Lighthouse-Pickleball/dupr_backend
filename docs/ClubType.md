# ClubType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_type_id** | **int** |  | 
**club_type** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from dupr_backend.models.club_type import ClubType

# TODO update the JSON string below
json = "{}"
# create an instance of ClubType from a JSON string
club_type_instance = ClubType.from_json(json)
# print the JSON string representation of the object
print(ClubType.to_json())

# convert the object into a dict
club_type_dict = club_type_instance.to_dict()
# create an instance of ClubType from a dict
club_type_from_dict = ClubType.from_dict(club_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


