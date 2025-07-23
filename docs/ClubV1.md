# ClubV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urn** | [**ClubV1Urn**](ClubV1Urn.md) |  | 
**club** | [**Club**](Club.md) |  | 

## Example

```python
from dupr_backend.models.club_v1 import ClubV1

# TODO update the JSON string below
json = "{}"
# create an instance of ClubV1 from a JSON string
club_v1_instance = ClubV1.from_json(json)
# print the JSON string representation of the object
print(ClubV1.to_json())

# convert the object into a dict
club_v1_dict = club_v1_instance.to_dict()
# create an instance of ClubV1 from a dict
club_v1_from_dict = ClubV1.from_dict(club_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


