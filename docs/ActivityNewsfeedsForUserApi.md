# dupr_backend.ActivityNewsfeedsForUserApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments**](ActivityNewsfeedsForUserApi.md#comments) | **GET** /activity/{version}/user/{feedId}/{postId}/comments | 
[**create_post**](ActivityNewsfeedsForUserApi.md#create_post) | **POST** /activity/{version}/user/{feedId} | 
[**delete_comment**](ActivityNewsfeedsForUserApi.md#delete_comment) | **DELETE** /activity/{version}/user/{feedId}/{postId}/react | 
[**edit_post**](ActivityNewsfeedsForUserApi.md#edit_post) | **PUT** /activity/{version}/user/{feedId}/{postId} | 
[**fetch_feeds**](ActivityNewsfeedsForUserApi.md#fetch_feeds) | **GET** /activity/{version}/user/{feedId} | 
[**follow**](ActivityNewsfeedsForUserApi.md#follow) | **POST** /activity/{version}/user/{feedId}/follow | 
[**get_following_info**](ActivityNewsfeedsForUserApi.md#get_following_info) | **GET** /activity/{version}/user/{feedId}/followingInfo | 
[**get_list_followers**](ActivityNewsfeedsForUserApi.md#get_list_followers) | **GET** /activity/{version}/user/{feedId}/followers | 
[**get_list_followings**](ActivityNewsfeedsForUserApi.md#get_list_followings) | **GET** /activity/{version}/user/{feedId}/followings | 
[**get_post_detail**](ActivityNewsfeedsForUserApi.md#get_post_detail) | **GET** /activity/{version}/user/{feedId}/{postId} | 
[**get_user_suggestion1**](ActivityNewsfeedsForUserApi.md#get_user_suggestion1) | **GET** /activity/{version}/user/{feedId}/user-suggestion | 
[**react**](ActivityNewsfeedsForUserApi.md#react) | **POST** /activity/{version}/user/{feedId}/{postId}/react | 
[**reactions**](ActivityNewsfeedsForUserApi.md#reactions) | **GET** /activity/{version}/user/{feedId}/{postId}/reactions | 
[**remove_post**](ActivityNewsfeedsForUserApi.md#remove_post) | **DELETE** /activity/{version}/user/{feedId}/{postId} | 
[**timeline**](ActivityNewsfeedsForUserApi.md#timeline) | **GET** /activity/{version}/user/{feedId}/timeline | 
[**unfollow**](ActivityNewsfeedsForUserApi.md#unfollow) | **DELETE** /activity/{version}/user/{feedId}/follow | 
[**update_comment**](ActivityNewsfeedsForUserApi.md#update_comment) | **PUT** /activity/{version}/user/{feedId}/{postId}/react | 


# **comments**
> ArrayWrapperPostReactionResponse comments(version, feed_id, post_id, limit=limit, ref=ref)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_post_reaction_response import ArrayWrapperPostReactionResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.comments(version, feed_id, post_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **limit** | **int**|  | [optional] 
 **ref** | **str**|  | [optional] 

### Return type

[**ArrayWrapperPostReactionResponse**](ArrayWrapperPostReactionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_post**
> SingleWrapperPostResponse create_post(version, feed_id, post_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.post_request import PostRequest
from dupr_backend.models.single_wrapper_post_response import SingleWrapperPostResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_request = dupr_backend.PostRequest() # PostRequest | 

    try:
        api_response = api_instance.create_post(version, feed_id, post_request)
        print("The response of ActivityNewsfeedsForUserApi->create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_request** | [**PostRequest**](PostRequest.md)|  | 

### Return type

[**SingleWrapperPostResponse**](SingleWrapperPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> SingleWrapperUnit delete_comment(version, feed_id, post_id, react_delete_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.react_delete_request import ReactDeleteRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    react_delete_request = dupr_backend.ReactDeleteRequest() # ReactDeleteRequest | 

    try:
        api_response = api_instance.delete_comment(version, feed_id, post_id, react_delete_request)
        print("The response of ActivityNewsfeedsForUserApi->delete_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **react_delete_request** | [**ReactDeleteRequest**](ReactDeleteRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_post**
> SingleWrapperPostResponse edit_post(version, feed_id, post_id, post_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.post_request import PostRequest
from dupr_backend.models.single_wrapper_post_response import SingleWrapperPostResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    post_request = dupr_backend.PostRequest() # PostRequest | 

    try:
        api_response = api_instance.edit_post(version, feed_id, post_id, post_request)
        print("The response of ActivityNewsfeedsForUserApi->edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **post_request** | [**PostRequest**](PostRequest.md)|  | 

### Return type

[**SingleWrapperPostResponse**](SingleWrapperPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feeds**
> ArrayWrapperPostResponse fetch_feeds(version, feed_id, limit=limit, ref=ref)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_post_response import ArrayWrapperPostResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.fetch_feeds(version, feed_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->fetch_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->fetch_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **limit** | **int**|  | [optional] 
 **ref** | **str**|  | [optional] 

### Return type

[**ArrayWrapperPostResponse**](ArrayWrapperPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow**
> Wrapper follow(version, feed_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id

    try:
        api_response = api_instance.follow(version, feed_id)
        print("The response of ActivityNewsfeedsForUserApi->follow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_following_info**
> SingleWrapperFollowingInfo get_following_info(version, feed_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_following_info import SingleWrapperFollowingInfo
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id

    try:
        api_response = api_instance.get_following_info(version, feed_id)
        print("The response of ActivityNewsfeedsForUserApi->get_following_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_following_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 

### Return type

[**SingleWrapperFollowingInfo**](SingleWrapperFollowingInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_followers**
> ArrayWrapperActivityUser get_list_followers(version, feed_id, limit=limit, offset=offset)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_activity_user import ArrayWrapperActivityUser
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.get_list_followers(version, feed_id, limit=limit, offset=offset)
        print("The response of ActivityNewsfeedsForUserApi->get_list_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_list_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ArrayWrapperActivityUser**](ArrayWrapperActivityUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_followings**
> ArrayWrapperActivityUser get_list_followings(version, feed_id, limit=limit, offset=offset)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_activity_user import ArrayWrapperActivityUser
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.get_list_followings(version, feed_id, limit=limit, offset=offset)
        print("The response of ActivityNewsfeedsForUserApi->get_list_followings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_list_followings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ArrayWrapperActivityUser**](ArrayWrapperActivityUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_detail**
> SingleWrapperPostResponse get_post_detail(version, feed_id, post_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_post_response import SingleWrapperPostResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id

    try:
        api_response = api_instance.get_post_detail(version, feed_id, post_id)
        print("The response of ActivityNewsfeedsForUserApi->get_post_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_post_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 

### Return type

[**SingleWrapperPostResponse**](SingleWrapperPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_suggestion1**
> SingleWrapperPageUserSuggestion get_user_suggestion1(version, feed_id, limit=limit, offset=offset)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_user_suggestion import SingleWrapperPageUserSuggestion
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.get_user_suggestion1(version, feed_id, limit=limit, offset=offset)
        print("The response of ActivityNewsfeedsForUserApi->get_user_suggestion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_user_suggestion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**SingleWrapperPageUserSuggestion**](SingleWrapperPageUserSuggestion.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react**
> SingleWrapperReaction react(version, feed_id, post_id, react_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.react_request import ReactRequest
from dupr_backend.models.single_wrapper_reaction import SingleWrapperReaction
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    react_request = dupr_backend.ReactRequest() # ReactRequest | 

    try:
        api_response = api_instance.react(version, feed_id, post_id, react_request)
        print("The response of ActivityNewsfeedsForUserApi->react:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->react: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **react_request** | [**ReactRequest**](ReactRequest.md)|  | 

### Return type

[**SingleWrapperReaction**](SingleWrapperReaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions**
> ArrayWrapperReaction reactions(version, feed_id, post_id, limit=limit, ref=ref)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_reaction import ArrayWrapperReaction
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.reactions(version, feed_id, post_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->reactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->reactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **limit** | **int**|  | [optional] 
 **ref** | **str**|  | [optional] 

### Return type

[**ArrayWrapperReaction**](ArrayWrapperReaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_post**
> SingleWrapperUnit remove_post(version, feed_id, post_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id

    try:
        api_response = api_instance.remove_post(version, feed_id, post_id)
        print("The response of ActivityNewsfeedsForUserApi->remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeline**
> ArrayWrapperPostResponse timeline(version, feed_id, limit=limit, ref=ref)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_post_response import ArrayWrapperPostResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.timeline(version, feed_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **limit** | **int**|  | [optional] 
 **ref** | **str**|  | [optional] 

### Return type

[**ArrayWrapperPostResponse**](ArrayWrapperPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow**
> Wrapper unfollow(version, feed_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id

    try:
        api_response = api_instance.unfollow(version, feed_id)
        print("The response of ActivityNewsfeedsForUserApi->unfollow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->unfollow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> Wrapper update_comment(version, feed_id, post_id, react_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.react_request import ReactRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    react_request = dupr_backend.ReactRequest() # ReactRequest | 

    try:
        api_response = api_instance.update_comment(version, feed_id, post_id, react_request)
        print("The response of ActivityNewsfeedsForUserApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **react_request** | [**ReactRequest**](ReactRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

