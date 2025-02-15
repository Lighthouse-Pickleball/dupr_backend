# GetClubRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.get_club_restrictions_request import GetClubRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetClubRestrictionsRequest from a JSON string
get_club_restrictions_request_instance = GetClubRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetClubRestrictionsRequest.to_json())

# convert the object into a dict
get_club_restrictions_request_dict = get_club_restrictions_request_instance.to_dict()
# create an instance of GetClubRestrictionsRequest from a dict
get_club_restrictions_request_from_dict = GetClubRestrictionsRequest.from_dict(get_club_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


