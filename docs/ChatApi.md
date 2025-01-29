# dupr_backend.ChatApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_token_using_get**](ChatApi.md#chat_token_using_get) | **GET** /chat/{version}/token/{id} | chatToken
[**get_self_token_using_get**](ChatApi.md#get_self_token_using_get) | **GET** /chat/{version}/token/self | getSelfToken
[**update_user_using_post**](ChatApi.md#update_user_using_post) | **POST** /chat/{version}/update/user | updateUser

# **chat_token_using_get**
> SingleWrapperOfChatTokenResponse chat_token_using_get(authorization, id, version)

chatToken

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ChatApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # chatToken
    api_response = api_instance.chat_token_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfChatTokenResponse**](SingleWrapperOfChatTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_token_using_get**
> SingleWrapperOfChatTokenResponse get_self_token_using_get(authorization, version)

getSelfToken

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ChatApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getSelfToken
    api_response = api_instance.get_self_token_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_self_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfChatTokenResponse**](SingleWrapperOfChatTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_post**
> Wrapper update_user_using_post(body, authorization, version)

updateUser

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ChatApi()
body = dupr_backend.UpdateUserRequest() # UpdateUserRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateUser
    api_response = api_instance.update_user_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->update_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

