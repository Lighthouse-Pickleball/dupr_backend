# ClubMemberManyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players_added** | **int** |  | 
**players_invited** | **int** |  | 
**invalid_email** | **int** |  | 
**add_members_action_s3_url** | **str** |  | [optional] 
**valid_email** | **List[str]** |  | [optional] 
**in_valid_email** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.club_member_many_response import ClubMemberManyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMemberManyResponse from a JSON string
club_member_many_response_instance = ClubMemberManyResponse.from_json(json)
# print the JSON string representation of the object
print(ClubMemberManyResponse.to_json())

# convert the object into a dict
club_member_many_response_dict = club_member_many_response_instance.to_dict()
# create an instance of ClubMemberManyResponse from a dict
club_member_many_response_from_dict = ClubMemberManyResponse.from_dict(club_member_many_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


