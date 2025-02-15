# RemoveClubRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 
**restrictions** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.remove_club_restrictions_request import RemoveClubRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveClubRestrictionsRequest from a JSON string
remove_club_restrictions_request_instance = RemoveClubRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveClubRestrictionsRequest.to_json())

# convert the object into a dict
remove_club_restrictions_request_dict = remove_club_restrictions_request_instance.to_dict()
# create an instance of RemoveClubRestrictionsRequest from a dict
remove_club_restrictions_request_from_dict = RemoveClubRestrictionsRequest.from_dict(remove_club_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


