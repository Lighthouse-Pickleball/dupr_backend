# ClubMembersRatingFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**doubles** | [**ClubMembersRatingRange**](ClubMembersRatingRange.md) |  | [optional] 
**singles** | [**ClubMembersRatingRange**](ClubMembersRatingRange.md) |  | [optional] 

## Example

```python
from dupr_backend.models.club_members_rating_filter import ClubMembersRatingFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMembersRatingFilter from a JSON string
club_members_rating_filter_instance = ClubMembersRatingFilter.from_json(json)
# print the JSON string representation of the object
print(ClubMembersRatingFilter.to_json())

# convert the object into a dict
club_members_rating_filter_dict = club_members_rating_filter_instance.to_dict()
# create an instance of ClubMembersRatingFilter from a dict
club_members_rating_filter_from_dict = ClubMembersRatingFilter.from_dict(club_members_rating_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


