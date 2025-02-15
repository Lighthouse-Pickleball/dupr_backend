# dupr_backend.ClientApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_name_by_key_using_get**](ClientApi.md#get_client_name_by_key_using_get) | **GET** /client/{version}/{clientKey}/name | getClientNameByKey


# **get_client_name_by_key_using_get**
> SingleWrapperOfstring get_client_name_by_key_using_get(authorization, client_key, version)

getClientNameByKey

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_ofstring import SingleWrapperOfstring
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ClientApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    client_key = 'client_key_example' # str | clientKey
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getClientNameByKey
        api_response = api_instance.get_client_name_by_key_using_get(authorization, client_key, version)
        print("The response of ClientApi->get_client_name_by_key_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->get_client_name_by_key_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **client_key** | **str**| clientKey | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

