# ClubMemberAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_members** | [**List[MemberRequest]**](MemberRequest.md) |  | 

## Example

```python
from dupr_backend.models.club_member_add_request import ClubMemberAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMemberAddRequest from a JSON string
club_member_add_request_instance = ClubMemberAddRequest.from_json(json)
# print the JSON string representation of the object
print(ClubMemberAddRequest.to_json())

# convert the object into a dict
club_member_add_request_dict = club_member_add_request_instance.to_dict()
# create an instance of ClubMemberAddRequest from a dict
club_member_add_request_from_dict = ClubMemberAddRequest.from_dict(club_member_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


