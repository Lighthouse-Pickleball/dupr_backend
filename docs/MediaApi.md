# dupr_backend.MediaApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_document_using_put**](MediaApi.md#upload_document_using_put) | **PUT** /media/{version}/document | uploadDocument
[**upload_using_put**](MediaApi.md#upload_using_put) | **PUT** /media/{version}/image | upload


# **upload_document_using_put**
> SingleWrapperOfMediaResponse upload_document_using_put(version)

uploadDocument

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_media_response import SingleWrapperOfMediaResponse
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
    api_instance = dupr_backend.MediaApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # uploadDocument
        api_response = api_instance.upload_document_using_put(version)
        print("The response of MediaApi->upload_document_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->upload_document_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfMediaResponse**](SingleWrapperOfMediaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_using_put**
> SingleWrapperOfMediaResponse upload_using_put(version)

upload

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_media_response import SingleWrapperOfMediaResponse
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
    api_instance = dupr_backend.MediaApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # upload
        api_response = api_instance.upload_using_put(version)
        print("The response of MediaApi->upload_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->upload_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfMediaResponse**](SingleWrapperOfMediaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

