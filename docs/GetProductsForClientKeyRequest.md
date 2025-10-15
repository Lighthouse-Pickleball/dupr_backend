# GetProductsForClientKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_client_key** | **str** |  | 

## Example

```python
from dupr_backend.models.get_products_for_client_key_request import GetProductsForClientKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsForClientKeyRequest from a JSON string
get_products_for_client_key_request_instance = GetProductsForClientKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GetProductsForClientKeyRequest.to_json())

# convert the object into a dict
get_products_for_client_key_request_dict = get_products_for_client_key_request_instance.to_dict()
# create an instance of GetProductsForClientKeyRequest from a dict
get_products_for_client_key_request_from_dict = GetProductsForClientKeyRequest.from_dict(get_products_for_client_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


