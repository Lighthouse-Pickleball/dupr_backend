# ClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**birthdate** | **str** |  | [optional] 
**club_id** | **int** |  | 
**created** | **str** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**doubles** | **str** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**doubles_reliability** | **float** |  | [optional] 
**doubles_verified** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**enable_privacy** | **bool** |  | 
**formatted_address** | **str** |  | [optional] 
**full_name** | **str** |  | 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | 
**image_url** | **str** |  | [optional] 
**invitation_type** | **str** |  | [optional] 
**is_checked** | **bool** |  | [optional] 
**iso_alpha2_code** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**location** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**phone** | **str** |  | [optional] 
**provisional_doubles_rating** | **float** |  | [optional] 
**provisional_singles_rating** | **float** |  | [optional] 
**requested_by** | **int** |  | [optional] 
**roles** | [**List[ClubRole]**](ClubRole.md) |  | 
**short_address** | **str** |  | [optional] 
**singles** | **str** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**singles_reliability** | **float** |  | [optional] 
**singles_verified** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified_email** | **bool** |  | [optional] 
**verified_phone** | **bool** |  | [optional] 

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


