# PostMatchRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubles** | **float** |  | [optional] 
**singles** | **float** |  | [optional] 

## Example

```python
from dupr_backend.models.post_match_rating import PostMatchRating

# TODO update the JSON string below
json = "{}"
# create an instance of PostMatchRating from a JSON string
post_match_rating_instance = PostMatchRating.from_json(json)
# print the JSON string representation of the object
print PostMatchRating.to_json()

# convert the object into a dict
post_match_rating_dict = post_match_rating_instance.to_dict()
# create an instance of PostMatchRating from a dict
post_match_rating_form_dict = post_match_rating.from_dict(post_match_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


