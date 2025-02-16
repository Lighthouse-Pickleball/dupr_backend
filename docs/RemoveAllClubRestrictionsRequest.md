# RemoveAllClubRestrictionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.remove_all_club_restrictions_request import RemoveAllClubRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAllClubRestrictionsRequest from a JSON string
remove_all_club_restrictions_request_instance = RemoveAllClubRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print RemoveAllClubRestrictionsRequest.to_json()

# convert the object into a dict
remove_all_club_restrictions_request_dict = remove_all_club_restrictions_request_instance.to_dict()
# create an instance of RemoveAllClubRestrictionsRequest from a dict
remove_all_club_restrictions_request_form_dict = remove_all_club_restrictions_request.from_dict(remove_all_club_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


