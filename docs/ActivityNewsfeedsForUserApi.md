# dupr_backend.ActivityNewsfeedsForUserApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_using_get1**](ActivityNewsfeedsForUserApi.md#comments_using_get1) | **GET** /activity/{version}/user/{feedId}/{postId}/comments | comments
[**create_post_using_post2**](ActivityNewsfeedsForUserApi.md#create_post_using_post2) | **POST** /activity/{version}/user/{feedId} | createPost
[**delete_comment_using_delete1**](ActivityNewsfeedsForUserApi.md#delete_comment_using_delete1) | **DELETE** /activity/{version}/user/{feedId}/{postId}/react | deleteComment
[**edit_post_using_put1**](ActivityNewsfeedsForUserApi.md#edit_post_using_put1) | **PUT** /activity/{version}/user/{feedId}/{postId} | editPost
[**fetch_feeds_using_get2**](ActivityNewsfeedsForUserApi.md#fetch_feeds_using_get2) | **GET** /activity/{version}/user/{feedId} | fetchFeeds
[**follow_using_post2**](ActivityNewsfeedsForUserApi.md#follow_using_post2) | **POST** /activity/{version}/user/{feedId}/follow | follow
[**get_following_info_using_get**](ActivityNewsfeedsForUserApi.md#get_following_info_using_get) | **GET** /activity/{version}/user/{feedId}/followingInfo | getFollowingInfo
[**get_list_followers_using_get**](ActivityNewsfeedsForUserApi.md#get_list_followers_using_get) | **GET** /activity/{version}/user/{feedId}/followers | getListFollowers
[**get_list_followings_using_get**](ActivityNewsfeedsForUserApi.md#get_list_followings_using_get) | **GET** /activity/{version}/user/{feedId}/followings | getListFollowings
[**get_post_detail_using_get1**](ActivityNewsfeedsForUserApi.md#get_post_detail_using_get1) | **GET** /activity/{version}/user/{feedId}/{postId} | getPostDetail
[**get_user_suggestion_using_get1**](ActivityNewsfeedsForUserApi.md#get_user_suggestion_using_get1) | **GET** /activity/{version}/user/{feedId}/user-suggestion | getUserSuggestion
[**react_using_post2**](ActivityNewsfeedsForUserApi.md#react_using_post2) | **POST** /activity/{version}/user/{feedId}/{postId}/react | react
[**reactions_using_get1**](ActivityNewsfeedsForUserApi.md#reactions_using_get1) | **GET** /activity/{version}/user/{feedId}/{postId}/reactions | reactions
[**remove_post_using_delete1**](ActivityNewsfeedsForUserApi.md#remove_post_using_delete1) | **DELETE** /activity/{version}/user/{feedId}/{postId} | removePost
[**timeline_using_get**](ActivityNewsfeedsForUserApi.md#timeline_using_get) | **GET** /activity/{version}/user/{feedId}/timeline | timeline
[**unfollow_using_delete2**](ActivityNewsfeedsForUserApi.md#unfollow_using_delete2) | **DELETE** /activity/{version}/user/{feedId}/follow | unfollow
[**update_comment_using_put1**](ActivityNewsfeedsForUserApi.md#update_comment_using_put1) | **PUT** /activity/{version}/user/{feedId}/{postId}/react | updateComment


# **comments_using_get1**
> ArrayWrapperOfPostReactionResponse comments_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)

comments

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # comments
        api_response = api_instance.comments_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->comments_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->comments_using_get1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **create_post_using_post2**
> SingleWrapperOfPostResponse create_post_using_post2(authorization, feed_id, version, request)

createPost

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PostRequest() # PostRequest | request

    try:
        # createPost
        api_response = api_instance.create_post_using_post2(authorization, feed_id, version, request)
        print("The response of ActivityNewsfeedsForUserApi->create_post_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->create_post_using_post2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **delete_comment_using_delete1**
> SingleWrapperOfUnit delete_comment_using_delete1(authorization, feed_id, post_id, version, react)

deleteComment

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    react = dupr_backend.ReactDeleteRequest() # ReactDeleteRequest | The react Id

    try:
        # deleteComment
        api_response = api_instance.delete_comment_using_delete1(authorization, feed_id, post_id, version, react)
        print("The response of ActivityNewsfeedsForUserApi->delete_comment_using_delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->delete_comment_using_delete1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **edit_post_using_put1**
> SingleWrapperOfPostResponse edit_post_using_put1(authorization, feed_id, post_id, version, post_request)

editPost

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    post_request = dupr_backend.PostRequest() # PostRequest | postRequest

    try:
        # editPost
        api_response = api_instance.edit_post_using_put1(authorization, feed_id, post_id, version, post_request)
        print("The response of ActivityNewsfeedsForUserApi->edit_post_using_put1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->edit_post_using_put1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **fetch_feeds_using_get2**
> ArrayWrapperOfPostResponse fetch_feeds_using_get2(authorization, feed_id, version, limit=limit, ref=ref)

fetchFeeds

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # fetchFeeds
        api_response = api_instance.fetch_feeds_using_get2(authorization, feed_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->fetch_feeds_using_get2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->fetch_feeds_using_get2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **follow_using_post2**
> Wrapper follow_using_post2(authorization, feed_id, version)

follow

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # follow
        api_response = api_instance.follow_using_post2(authorization, feed_id, version)
        print("The response of ActivityNewsfeedsForUserApi->follow_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->follow_using_post2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **get_following_info_using_get**
> SingleWrapperOfFollowingInfo get_following_info_using_get(authorization, feed_id, version)

getFollowingInfo

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_following_info import SingleWrapperOfFollowingInfo
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getFollowingInfo
        api_response = api_instance.get_following_info_using_get(authorization, feed_id, version)
        print("The response of ActivityNewsfeedsForUserApi->get_following_info_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_following_info_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfFollowingInfo**](SingleWrapperOfFollowingInfo.md)

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

# **get_list_followers_using_get**
> ArrayWrapperOfActivityUser get_list_followers_using_get(authorization, feed_id, version, limit=limit, offset=offset)

getListFollowers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_activity_user import ArrayWrapperOfActivityUser
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)

    try:
        # getListFollowers
        api_response = api_instance.get_list_followers_using_get(authorization, feed_id, version, limit=limit, offset=offset)
        print("The response of ActivityNewsfeedsForUserApi->get_list_followers_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_list_followers_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**ArrayWrapperOfActivityUser**](ArrayWrapperOfActivityUser.md)

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

# **get_list_followings_using_get**
> ArrayWrapperOfActivityUser get_list_followings_using_get(authorization, feed_id, version, limit=limit, offset=offset)

getListFollowings

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_activity_user import ArrayWrapperOfActivityUser
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)

    try:
        # getListFollowings
        api_response = api_instance.get_list_followings_using_get(authorization, feed_id, version, limit=limit, offset=offset)
        print("The response of ActivityNewsfeedsForUserApi->get_list_followings_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_list_followings_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**ArrayWrapperOfActivityUser**](ArrayWrapperOfActivityUser.md)

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

# **get_post_detail_using_get1**
> SingleWrapperOfPostResponse get_post_detail_using_get1(authorization, feed_id, post_id, version)

getPostDetail

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getPostDetail
        api_response = api_instance.get_post_detail_using_get1(authorization, feed_id, post_id, version)
        print("The response of ActivityNewsfeedsForUserApi->get_post_detail_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_post_detail_using_get1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **get_user_suggestion_using_get1**
> SingleWrapperOfPageOfUserSuggestion get_user_suggestion_using_get1(authorization, feed_id, version, limit=limit, offset=offset)

getUserSuggestion

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_user_suggestion import SingleWrapperOfPageOfUserSuggestion
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)

    try:
        # getUserSuggestion
        api_response = api_instance.get_user_suggestion_using_get1(authorization, feed_id, version, limit=limit, offset=offset)
        print("The response of ActivityNewsfeedsForUserApi->get_user_suggestion_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->get_user_suggestion_using_get1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfUserSuggestion**](SingleWrapperOfPageOfUserSuggestion.md)

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

# **react_using_post2**
> SingleWrapperOfReaction react_using_post2(authorization, feed_id, post_id, version, request)

react

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ReactRequest() # ReactRequest | request

    try:
        # react
        api_response = api_instance.react_using_post2(authorization, feed_id, post_id, version, request)
        print("The response of ActivityNewsfeedsForUserApi->react_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->react_using_post2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **reactions_using_get1**
> ArrayWrapperOfReaction reactions_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)

reactions

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # reactions
        api_response = api_instance.reactions_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->reactions_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->reactions_using_get1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **remove_post_using_delete1**
> SingleWrapperOfUnit remove_post_using_delete1(authorization, feed_id, post_id, version)

removePost

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # removePost
        api_response = api_instance.remove_post_using_delete1(authorization, feed_id, post_id, version)
        print("The response of ActivityNewsfeedsForUserApi->remove_post_using_delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->remove_post_using_delete1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **timeline_using_get**
> ArrayWrapperOfPostResponse timeline_using_get(authorization, feed_id, version, limit=limit, ref=ref)

timeline

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    ref = 'ref_example' # str | ref (optional)

    try:
        # timeline
        api_response = api_instance.timeline_using_get(authorization, feed_id, version, limit=limit, ref=ref)
        print("The response of ActivityNewsfeedsForUserApi->timeline_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->timeline_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **unfollow_using_delete2**
> Wrapper unfollow_using_delete2(authorization, feed_id, version)

unfollow

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # unfollow
        api_response = api_instance.unfollow_using_delete2(authorization, feed_id, version)
        print("The response of ActivityNewsfeedsForUserApi->unfollow_using_delete2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->unfollow_using_delete2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

# **update_comment_using_put1**
> Wrapper update_comment_using_put1(authorization, feed_id, post_id, version, request)

updateComment

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ActivityNewsfeedsForUserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    feed_id = 56 # int | The user's feed Id
    post_id = 'post_id_example' # str | The post Id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ReactRequest() # ReactRequest | request

    try:
        # updateComment
        api_response = api_instance.update_comment_using_put1(authorization, feed_id, post_id, version, request)
        print("The response of ActivityNewsfeedsForUserApi->update_comment_using_put1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNewsfeedsForUserApi->update_comment_using_put1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **feed_id** | **int**| The user&#39;s feed Id | 
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

