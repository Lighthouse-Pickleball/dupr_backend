# BatchPlayerRatingProvisionalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**key** | **str** |  | 

## Example

```python
from dupr_backend.models.batch_player_rating_provisional_request import BatchPlayerRatingProvisionalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPlayerRatingProvisionalRequest from a JSON string
batch_player_rating_provisional_request_instance = BatchPlayerRatingProvisionalRequest.from_json(json)
# print the JSON string representation of the object
print(BatchPlayerRatingProvisionalRequest.to_json())

# convert the object into a dict
batch_player_rating_provisional_request_dict = batch_player_rating_provisional_request_instance.to_dict()
# create an instance of BatchPlayerRatingProvisionalRequest from a dict
batch_player_rating_provisional_request_from_dict = BatchPlayerRatingProvisionalRequest.from_dict(batch_player_rating_provisional_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


