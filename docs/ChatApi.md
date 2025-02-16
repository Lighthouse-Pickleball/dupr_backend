# dupr_backend.ChatApi

All URIs are relative to *http://https://backend.mydupr.com*

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
import dupr_backend
from dupr_backend.models.single_wrapper_of_chat_token_response import SingleWrapperOfChatTokenResponse
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
    api_instance = dupr_backend.ChatApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # chatToken
        api_response = api_instance.chat_token_using_get(authorization, id, version)
        print("The response of ChatApi->chat_token_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat_token_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfChatTokenResponse**](SingleWrapperOfChatTokenResponse.md)

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

# **get_self_token_using_get**
> SingleWrapperOfChatTokenResponse get_self_token_using_get(authorization, version)

getSelfToken

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_chat_token_response import SingleWrapperOfChatTokenResponse
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
    api_instance = dupr_backend.ChatApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getSelfToken
        api_response = api_instance.get_self_token_using_get(authorization, version)
        print("The response of ChatApi->get_self_token_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_self_token_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfChatTokenResponse**](SingleWrapperOfChatTokenResponse.md)

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

# **update_user_using_post**
> Wrapper update_user_using_post(authorization, version, request)

updateUser

### Example


```python
import dupr_backend
from dupr_backend.models.update_user_request import UpdateUserRequest
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.ChatApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UpdateUserRequest() # UpdateUserRequest | request

    try:
        # updateUser
        api_response = api_instance.update_user_using_post(authorization, version, request)
        print("The response of ChatApi->update_user_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->update_user_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

