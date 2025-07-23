# ClubMembersRatingRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_rating** | **float** |  | 
**max_rating** | **float** |  | 

## Example

```python
from dupr_backend.models.club_members_rating_range import ClubMembersRatingRange

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMembersRatingRange from a JSON string
club_members_rating_range_instance = ClubMembersRatingRange.from_json(json)
# print the JSON string representation of the object
print(ClubMembersRatingRange.to_json())

# convert the object into a dict
club_members_rating_range_dict = club_members_rating_range_instance.to_dict()
# create an instance of ClubMembersRatingRange from a dict
club_members_rating_range_from_dict = ClubMembersRatingRange.from_dict(club_members_rating_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


