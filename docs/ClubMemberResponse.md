# ClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**full_name** | **str** |  | 
**username** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**verified_email** | **bool** |  | [optional] 
**iso_alpha2_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**verified_phone** | **bool** |  | [optional] 
**short_address** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**gender** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**age** | **int** |  | [optional] 
**hand** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**singles** | **str** |  | [optional] 
**singles_verified** | **str** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**doubles** | **str** |  | [optional] 
**doubles_verified** | **str** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**enable_privacy** | **bool** |  | 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**club_id** | **int** |  | 
**roles** | [**List[ClubRole]**](ClubRole.md) |  | 
**requested_by** | **int** |  | [optional] 
**invitation_type** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**is_checked** | **bool** |  | [optional] 
**provisional_singles_rating** | **float** |  | [optional] 
**provisional_doubles_rating** | **float** |  | [optional] 
**singles_reliability** | **float** |  | [optional] 
**doubles_reliability** | **float** |  | [optional] 
**location** | **str** |  | [optional] 
**checked** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.club_member_response import ClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMemberResponse from a JSON string
club_member_response_instance = ClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print(ClubMemberResponse.to_json())

# convert the object into a dict
club_member_response_dict = club_member_response_instance.to_dict()
# create an instance of ClubMemberResponse from a dict
club_member_response_from_dict = ClubMemberResponse.from_dict(club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


