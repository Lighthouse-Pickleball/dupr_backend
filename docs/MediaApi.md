# dupr_backend.MediaApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_document_using_put**](MediaApi.md#upload_document_using_put) | **PUT** /media/{version}/document | uploadDocument
[**upload_using_put**](MediaApi.md#upload_using_put) | **PUT** /media/{version}/image | upload

# **upload_document_using_put**
> SingleWrapperOfMediaResponse upload_document_using_put(version)

uploadDocument

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MediaApi()
version = 'version_example' # str | version

try:
    # uploadDocument
    api_response = api_instance.upload_document_using_put(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->upload_document_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMediaResponse**](SingleWrapperOfMediaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_using_put**
> SingleWrapperOfMediaResponse upload_using_put(version)

upload

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MediaApi()
version = 'version_example' # str | version

try:
    # upload
    api_response = api_instance.upload_using_put(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->upload_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMediaResponse**](SingleWrapperOfMediaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

