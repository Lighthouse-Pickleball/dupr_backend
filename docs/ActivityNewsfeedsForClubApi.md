# dupr_backend.ActivityNewsfeedsForClubApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_using_get**](ActivityNewsfeedsForClubApi.md#comments_using_get) | **GET** /activity/{version}/club/{feedId}/{postId}/comments | comments
[**create_post_using_post1**](ActivityNewsfeedsForClubApi.md#create_post_using_post1) | **POST** /activity/{version}/club/{feedId} | createPost
[**delete_comment_using_delete**](ActivityNewsfeedsForClubApi.md#delete_comment_using_delete) | **DELETE** /activity/{version}/club/{feedId}/{postId}/react | deleteComment
[**edit_post_using_put**](ActivityNewsfeedsForClubApi.md#edit_post_using_put) | **PUT** /activity/{version}/club/{feedId}/{postId} | editPost
[**fetch_feeds_using_get1**](ActivityNewsfeedsForClubApi.md#fetch_feeds_using_get1) | **GET** /activity/{version}/club/{feedId} | fetchFeeds
[**follow_using_post1**](ActivityNewsfeedsForClubApi.md#follow_using_post1) | **POST** /activity/{version}/club/{feedId}/follow | follow
[**get_pinned_posts_using_get**](ActivityNewsfeedsForClubApi.md#get_pinned_posts_using_get) | **GET** /activity/{version}/club/{feedId}/pinned | getPinnedPosts
[**get_post_detail_using_get**](ActivityNewsfeedsForClubApi.md#get_post_detail_using_get) | **GET** /activity/{version}/club/{feedId}/{postId} | getPostDetail
[**pin_post_using_post**](ActivityNewsfeedsForClubApi.md#pin_post_using_post) | **POST** /activity/{version}/club/{feedId}/{postId}/pin | pinPost
[**react_using_post1**](ActivityNewsfeedsForClubApi.md#react_using_post1) | **POST** /activity/{version}/club/{feedId}/{postId}/react | react
[**reactions_using_get**](ActivityNewsfeedsForClubApi.md#reactions_using_get) | **GET** /activity/{version}/club/{feedId}/{postId}/reactions | reactions
[**remove_post_using_delete**](ActivityNewsfeedsForClubApi.md#remove_post_using_delete) | **DELETE** /activity/{version}/club/{feedId}/{postId} | removePost
[**unfollow_using_delete1**](ActivityNewsfeedsForClubApi.md#unfollow_using_delete1) | **DELETE** /activity/{version}/club/{feedId}/follow | unfollow
[**unpin_post_using_delete**](ActivityNewsfeedsForClubApi.md#unpin_post_using_delete) | **DELETE** /activity/{version}/club/{feedId}/{postId}/pin | unpinPost
[**update_comment_using_put**](ActivityNewsfeedsForClubApi.md#update_comment_using_put) | **PUT** /activity/{version}/club/{feedId}/{postId}/react | updateComment


# **comments_using_get**
> ArrayWrapperOfPostReactionResponse comments_using_get(authorization, feed_id, post_id, version, limit=limit, ref=ref)

comments

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_post_reaction_response import ArrayWrapperOfPostReactionResponse
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # comments
        api_response = api_instance.comments_using_get(authorization, feed_id, post_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForClubApi->comments_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->comments_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfPostReactionResponse**](ArrayWrapperOfPostReactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_post_using_post1**
> SingleWrapperOfPostResponse create_post_using_post1(authorization, feed_id, version, request)

createPost

### Example


```python
import dupr_backend
from dupr_backend.models.post_request import PostRequest
from dupr_backend.models.single_wrapper_of_post_response import SingleWrapperOfPostResponse
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PostRequest() # PostRequest | request

    try:
        # createPost
        api_response = api_instance.create_post_using_post1(authorization, feed_id, version, request)
        print("The response of ActivityNewsfeedsForClubApi->create_post_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->create_post_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PostRequest**](PostRequest.md)| request | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

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

# **delete_comment_using_delete**
> SingleWrapperOfUnit delete_comment_using_delete(authorization, feed_id, post_id, version, react)

deleteComment

### Example


```python
import dupr_backend
from dupr_backend.models.react_delete_request import ReactDeleteRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    react = dupr_backend.ReactDeleteRequest() # ReactDeleteRequest | The react Id

    try:
        # deleteComment
        api_response = api_instance.delete_comment_using_delete(authorization, feed_id, post_id, version, react)
        print("The response of ActivityNewsfeedsForClubApi->delete_comment_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->delete_comment_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **react** | [**ReactDeleteRequest**](ReactDeleteRequest.md)| The react Id | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_post_using_put**
> SingleWrapperOfPostResponse edit_post_using_put(authorization, feed_id, post_id, version, post_request)

editPost

### Example


```python
import dupr_backend
from dupr_backend.models.post_request import PostRequest
from dupr_backend.models.single_wrapper_of_post_response import SingleWrapperOfPostResponse
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    post_request = dupr_backend.PostRequest() # PostRequest | postRequest

    try:
        # editPost
        api_response = api_instance.edit_post_using_put(authorization, feed_id, post_id, version, post_request)
        print("The response of ActivityNewsfeedsForClubApi->edit_post_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->edit_post_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **post_request** | [**PostRequest**](PostRequest.md)| postRequest | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feeds_using_get1**
> ArrayWrapperOfPostResponse fetch_feeds_using_get1(authorization, feed_id, version, limit=limit, ref=ref)

fetchFeeds

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_post_response import ArrayWrapperOfPostResponse
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # fetchFeeds
        api_response = api_instance.fetch_feeds_using_get1(authorization, feed_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForClubApi->fetch_feeds_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->fetch_feeds_using_get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfPostResponse**](ArrayWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_using_post1**
> Wrapper follow_using_post1(authorization, feed_id, version)

follow

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # follow
        api_response = api_instance.follow_using_post1(authorization, feed_id, version)
        print("The response of ActivityNewsfeedsForClubApi->follow_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->follow_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned_posts_using_get**
> ArrayWrapperOfPostResponse get_pinned_posts_using_get(authorization, feed_id, version, limit=limit)

getPinnedPosts

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_post_response import ArrayWrapperOfPostResponse
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)

    try:
        # getPinnedPosts
        api_response = api_instance.get_pinned_posts_using_get(authorization, feed_id, version, limit=limit)
        print("The response of ActivityNewsfeedsForClubApi->get_pinned_posts_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->get_pinned_posts_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]

### Return type

[**ArrayWrapperOfPostResponse**](ArrayWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_detail_using_get**
> SingleWrapperOfPostResponse get_post_detail_using_get(authorization, feed_id, post_id, version)

getPostDetail

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_post_response import SingleWrapperOfPostResponse
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getPostDetail
        api_response = api_instance.get_post_detail_using_get(authorization, feed_id, post_id, version)
        print("The response of ActivityNewsfeedsForClubApi->get_post_detail_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->get_post_detail_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_post_using_post**
> SingleWrapperOfUnit pin_post_using_post(authorization, feed_id, post_id, version)

pinPost

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # pinPost
        api_response = api_instance.pin_post_using_post(authorization, feed_id, post_id, version)
        print("The response of ActivityNewsfeedsForClubApi->pin_post_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->pin_post_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react_using_post1**
> SingleWrapperOfReaction react_using_post1(authorization, feed_id, post_id, version, request)

react

### Example


```python
import dupr_backend
from dupr_backend.models.react_request import ReactRequest
from dupr_backend.models.single_wrapper_of_reaction import SingleWrapperOfReaction
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ReactRequest() # ReactRequest | request

    try:
        # react
        api_response = api_instance.react_using_post1(authorization, feed_id, post_id, version, request)
        print("The response of ActivityNewsfeedsForClubApi->react_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->react_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ReactRequest**](ReactRequest.md)| request | 

### Return type

[**SingleWrapperOfReaction**](SingleWrapperOfReaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_using_get**
> ArrayWrapperOfReaction reactions_using_get(authorization, feed_id, post_id, version, limit=limit, ref=ref)

reactions

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_reaction import ArrayWrapperOfReaction
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # reactions
        api_response = api_instance.reactions_using_get(authorization, feed_id, post_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForClubApi->reactions_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->reactions_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfReaction**](ArrayWrapperOfReaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_post_using_delete**
> SingleWrapperOfUnit remove_post_using_delete(authorization, feed_id, post_id, version)

removePost

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # removePost
        api_response = api_instance.remove_post_using_delete(authorization, feed_id, post_id, version)
        print("The response of ActivityNewsfeedsForClubApi->remove_post_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->remove_post_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_using_delete1**
> Wrapper unfollow_using_delete1(authorization, feed_id, version)

unfollow

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # unfollow
        api_response = api_instance.unfollow_using_delete1(authorization, feed_id, version)
        print("The response of ActivityNewsfeedsForClubApi->unfollow_using_delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->unfollow_using_delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpin_post_using_delete**
> SingleWrapperOfUnit unpin_post_using_delete(authorization, feed_id, post_id, version)

unpinPost

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # unpinPost
        api_response = api_instance.unpin_post_using_delete(authorization, feed_id, post_id, version)
        print("The response of ActivityNewsfeedsForClubApi->unpin_post_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->unpin_post_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment_using_put**
> Wrapper update_comment_using_put(authorization, feed_id, post_id, version, request)

updateComment

### Example


```python
import dupr_backend
from dupr_backend.models.react_request import ReactRequest
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
    api_instance = dupr_backend.ActivityNewsfeedsForClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The club's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ReactRequest() # ReactRequest | request

    try:
        # updateComment
        api_response = api_instance.update_comment_using_put(authorization, feed_id, post_id, version, request)
        print("The response of ActivityNewsfeedsForClubApi->update_comment_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForClubApi->update_comment_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The club&#39;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ReactRequest**](ReactRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

