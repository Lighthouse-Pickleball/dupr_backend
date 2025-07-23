# ClubTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_type_id** | **int** |  | 
**club_type** | **str** |  | 

## Example

```python
from dupr_backend.models.club_type_response import ClubTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubTypeResponse from a JSON string
club_type_response_instance = ClubTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ClubTypeResponse.to_json())

# convert the object into a dict
club_type_response_dict = club_type_response_instance.to_dict()
# create an instance of ClubTypeResponse from a dict
club_type_response_from_dict = ClubTypeResponse.from_dict(club_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


