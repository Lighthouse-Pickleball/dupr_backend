# SetClubRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**restrictions** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.set_club_restrictions_request import SetClubRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetClubRestrictionsRequest from a JSON string
set_club_restrictions_request_instance = SetClubRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetClubRestrictionsRequest.to_json())

# convert the object into a dict
set_club_restrictions_request_dict = set_club_restrictions_request_instance.to_dict()
# create an instance of SetClubRestrictionsRequest from a dict
set_club_restrictions_request_from_dict = SetClubRestrictionsRequest.from_dict(set_club_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


