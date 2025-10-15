# ResultGetActiveProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | [**List[GetActiveProductsResponse]**](GetActiveProductsResponse.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_get_active_products_response import ResultGetActiveProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultGetActiveProductsResponse from a JSON string
result_get_active_products_response_instance = ResultGetActiveProductsResponse.from_json(json)
# print the JSON string representation of the object
print(ResultGetActiveProductsResponse.to_json())

# convert the object into a dict
result_get_active_products_response_dict = result_get_active_products_response_instance.to_dict()
# create an instance of ResultGetActiveProductsResponse from a dict
result_get_active_products_response_from_dict = ResultGetActiveProductsResponse.from_dict(result_get_active_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


