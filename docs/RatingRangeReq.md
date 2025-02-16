# RatingRangeReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** |  | 
**min** | **float** |  | 

## Example

```python
from dupr_backend.models.rating_range_req import RatingRangeReq

# TODO update the JSON string below
json = "{}"
# create an instance of RatingRangeReq from a JSON string
rating_range_req_instance = RatingRangeReq.from_json(json)
# print the JSON string representation of the object
print RatingRangeReq.to_json()

# convert the object into a dict
rating_range_req_dict = rating_range_req_instance.to_dict()
# create an instance of RatingRangeReq from a dict
rating_range_req_form_dict = rating_range_req.from_dict(rating_range_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


