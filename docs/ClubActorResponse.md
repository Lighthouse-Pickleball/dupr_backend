# ClubActorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_v1** | [**ClubV1**](ClubV1.md) |  | 

## Example

```python
from dupr_backend.models.club_actor_response import ClubActorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubActorResponse from a JSON string
club_actor_response_instance = ClubActorResponse.from_json(json)
# print the JSON string representation of the object
print(ClubActorResponse.to_json())

# convert the object into a dict
club_actor_response_dict = club_actor_response_instance.to_dict()
# create an instance of ClubActorResponse from a dict
club_actor_response_from_dict = ClubActorResponse.from_dict(club_actor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


