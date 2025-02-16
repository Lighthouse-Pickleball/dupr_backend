# BatchPlayerRatingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**event** | **str** |  | 
**key** | **str** |  | 

## Example

```python
from dupr_backend.models.batch_player_rating_request import BatchPlayerRatingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPlayerRatingRequest from a JSON string
batch_player_rating_request_instance = BatchPlayerRatingRequest.from_json(json)
# print the JSON string representation of the object
print BatchPlayerRatingRequest.to_json()

# convert the object into a dict
batch_player_rating_request_dict = batch_player_rating_request_instance.to_dict()
# create an instance of BatchPlayerRatingRequest from a dict
batch_player_rating_request_form_dict = batch_player_rating_request.from_dict(batch_player_rating_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


