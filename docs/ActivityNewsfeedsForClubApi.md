# dupr_backend.ActivityNewsfeedsForClubApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments1**](ActivityNewsfeedsForClubApi.md#comments1) | **GET** /activity/{version}/club/{feedId}/{postId}/comments | 
[**create_post1**](ActivityNewsfeedsForClubApi.md#create_post1) | **POST** /activity/{version}/club/{feedId} | 
[**delete_comment1**](ActivityNewsfeedsForClubApi.md#delete_comment1) | **DELETE** /activity/{version}/club/{feedId}/{postId}/react | 
[**edit_post1**](ActivityNewsfeedsForClubApi.md#edit_post1) | **PUT** /activity/{version}/club/{feedId}/{postId} | 
[**fetch_feeds1**](ActivityNewsfeedsForClubApi.md#fetch_feeds1) | **GET** /activity/{version}/club/{feedId} | 
[**follow1**](ActivityNewsfeedsForClubApi.md#follow1) | **POST** /activity/{version}/club/{feedId}/follow | 
[**get_pinned_posts**](ActivityNewsfeedsForClubApi.md#get_pinned_posts) | **GET** /activity/{version}/club/{feedId}/pinned | 
[**get_post_detail1**](ActivityNewsfeedsForClubApi.md#get_post_detail1) | **GET** /activity/{version}/club/{feedId}/{postId} | 
[**pin_post**](ActivityNewsfeedsForClubApi.md#pin_post) | **POST** /activity/{version}/club/{feedId}/{postId}/pin | 
[**react1**](ActivityNewsfeedsForClubApi.md#react1) | **POST** /activity/{version}/club/{feedId}/{postId}/react | 
[**reactions1**](ActivityNewsfeedsForClubApi.md#reactions1) | **GET** /activity/{version}/club/{feedId}/{postId}/reactions | 
[**remove_post1**](ActivityNewsfeedsForClubApi.md#remove_post1) | **DELETE** /activity/{version}/club/{feedId}/{postId} | 
[**unfollow1**](ActivityNewsfeedsForClubApi.md#unfollow1) | **DELETE** /activity/{version}/club/{feedId}/follow | 
[**unpin_post**](ActivityNewsfeedsForClubApi.md#unpin_post) | **DELETE** /activity/{version}/club/{feedId}/{postId}/pin | 
[**update_comment1**](ActivityNewsfeedsForClubApi.md#update_comment1) | **PUT** /activity/{version}/club/{feedId}/{postId}/react | 


# **comments1**
> ArrayWrapperPostReactionResponse comments1(version, feed_id, post_id, limit=limit, ref=ref)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.comments1(version, feed_id, post_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForClubApi->comments1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->comments1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **create_post1**
> SingleWrapperPostResponse create_post1(version, feed_id, post_request)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_request = dupr_backend.PostRequest() # PostRequest | 

    try:
        api_response = api_instance.create_post1(version, feed_id, post_request)
        print("The response of ActivityNewsfeedsForClubApi->create_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->create_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **delete_comment1**
> SingleWrapperUnit delete_comment1(version, feed_id, post_id, react_delete_request)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    react_delete_request = dupr_backend.ReactDeleteRequest() # ReactDeleteRequest | 

    try:
        api_response = api_instance.delete_comment1(version, feed_id, post_id, react_delete_request)
        print("The response of ActivityNewsfeedsForClubApi->delete_comment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->delete_comment1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **edit_post1**
> SingleWrapperPostResponse edit_post1(version, feed_id, post_id, post_request)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    post_request = dupr_backend.PostRequest() # PostRequest | 

    try:
        api_response = api_instance.edit_post1(version, feed_id, post_id, post_request)
        print("The response of ActivityNewsfeedsForClubApi->edit_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->edit_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **fetch_feeds1**
> ArrayWrapperPostResponse fetch_feeds1(version, feed_id, limit=limit, ref=ref)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.fetch_feeds1(version, feed_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForClubApi->fetch_feeds1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->fetch_feeds1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **follow1**
> Wrapper follow1(version, feed_id)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id

    try:
        api_response = api_instance.follow1(version, feed_id)
        print("The response of ActivityNewsfeedsForClubApi->follow1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->follow1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 

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

# **get_pinned_posts**
> ArrayWrapperPostResponse get_pinned_posts(version, feed_id, limit=limit)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_pinned_posts(version, feed_id, limit=limit)
        print("The response of ActivityNewsfeedsForClubApi->get_pinned_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->get_pinned_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **limit** | **int**|  | [optional] 

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

# **get_post_detail1**
> SingleWrapperPostResponse get_post_detail1(version, feed_id, post_id)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id

    try:
        api_response = api_instance.get_post_detail1(version, feed_id, post_id)
        print("The response of ActivityNewsfeedsForClubApi->get_post_detail1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->get_post_detail1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **pin_post**
> SingleWrapperUnit pin_post(version, feed_id, post_id)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id

    try:
        api_response = api_instance.pin_post(version, feed_id, post_id)
        print("The response of ActivityNewsfeedsForClubApi->pin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->pin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **react1**
> SingleWrapperReaction react1(version, feed_id, post_id, react_request)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    react_request = dupr_backend.ReactRequest() # ReactRequest | 

    try:
        api_response = api_instance.react1(version, feed_id, post_id, react_request)
        print("The response of ActivityNewsfeedsForClubApi->react1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->react1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **reactions1**
> ArrayWrapperReaction reactions1(version, feed_id, post_id, limit=limit, ref=ref)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.reactions1(version, feed_id, post_id, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForClubApi->reactions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->reactions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **remove_post1**
> SingleWrapperUnit remove_post1(version, feed_id, post_id)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id

    try:
        api_response = api_instance.remove_post1(version, feed_id, post_id)
        print("The response of ActivityNewsfeedsForClubApi->remove_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->remove_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **unfollow1**
> Wrapper unfollow1(version, feed_id)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id

    try:
        api_response = api_instance.unfollow1(version, feed_id)
        print("The response of ActivityNewsfeedsForClubApi->unfollow1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->unfollow1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 

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

# **unpin_post**
> SingleWrapperUnit unpin_post(version, feed_id, post_id)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id

    try:
        api_response = api_instance.unpin_post(version, feed_id, post_id)
        print("The response of ActivityNewsfeedsForClubApi->unpin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->unpin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

# **update_comment1**
> Wrapper update_comment1(version, feed_id, post_id, react_request)

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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    react_request = dupr_backend.ReactRequest() # ReactRequest | 

    try:
        api_response = api_instance.update_comment1(version, feed_id, post_id, react_request)
        print("The response of ActivityNewsfeedsForClubApi->update_comment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->update_comment1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
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

