# ClubV1Urn


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
from dupr_backend.models.club_v1_urn import ClubV1Urn

# TODO update the JSON string below
json = "{}"
# create an instance of ClubV1Urn from a JSON string
club_v1_urn_instance = ClubV1Urn.from_json(json)
# print the JSON string representation of the object
print(ClubV1Urn.to_json())

# convert the object into a dict
club_v1_urn_dict = club_v1_urn_instance.to_dict()
# create an instance of ClubV1Urn from a dict
club_v1_urn_from_dict = ClubV1Urn.from_dict(club_v1_urn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


