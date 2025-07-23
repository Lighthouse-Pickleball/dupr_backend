# ClubMembersAgeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_age** | **float** |  | 
**max_age** | **float** |  | 

## Example

```python
from dupr_backend.models.club_members_age_filter import ClubMembersAgeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMembersAgeFilter from a JSON string
club_members_age_filter_instance = ClubMembersAgeFilter.from_json(json)
# print the JSON string representation of the object
print(ClubMembersAgeFilter.to_json())

# convert the object into a dict
club_members_age_filter_dict = club_members_age_filter_instance.to_dict()
# create an instance of ClubMembersAgeFilter from a dict
club_members_age_filter_from_dict = ClubMembersAgeFilter.from_dict(club_members_age_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


