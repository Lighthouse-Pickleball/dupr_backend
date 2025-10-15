# GetActiveProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotions** | **Dict[str, List[DuprProduct]]** |  | 

## Example

```python
from dupr_backend.models.get_active_products_response import GetActiveProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActiveProductsResponse from a JSON string
get_active_products_response_instance = GetActiveProductsResponse.from_json(json)
# print the JSON string representation of the object
print(GetActiveProductsResponse.to_json())

# convert the object into a dict
get_active_products_response_dict = get_active_products_response_instance.to_dict()
# create an instance of GetActiveProductsResponse from a dict
get_active_products_response_from_dict = GetActiveProductsResponse.from_dict(get_active_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


