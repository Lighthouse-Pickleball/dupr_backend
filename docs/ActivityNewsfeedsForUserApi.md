# dupr_backend.ActivityNewsfeedsForUserApi

All URIs are relative to *//https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
ref = 'ref_example' # str | ref (optional)

try:
    # comments
    api_response = api_instance.comments_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->comments_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfPostReactionResponse**](ArrayWrapperOfPostReactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_post_using_post2**
> SingleWrapperOfPostResponse create_post_using_post2(body, authorization, feed_id, version)

createPost

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
body = dupr_backend.PostRequest() # PostRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version

try:
    # createPost
    api_response = api_instance.create_post_using_post2(body, authorization, feed_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->create_post_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRequest**](PostRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_using_delete1**
> SingleWrapperOfUnit delete_comment_using_delete1(body, authorization, feed_id, post_id, version)

deleteComment

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
body = dupr_backend.ReactDeleteRequest() # ReactDeleteRequest | The react Id
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version

try:
    # deleteComment
    api_response = api_instance.delete_comment_using_delete1(body, authorization, feed_id, post_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->delete_comment_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReactDeleteRequest**](ReactDeleteRequest.md)| The react Id | 
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_post_using_put1**
> SingleWrapperOfPostResponse edit_post_using_put1(body, authorization, feed_id, post_id, version)

editPost

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
body = dupr_backend.PostRequest() # PostRequest | postRequest
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version

try:
    # editPost
    api_response = api_instance.edit_post_using_put1(body, authorization, feed_id, post_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->edit_post_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRequest**](PostRequest.md)| postRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feeds_using_get2**
> ArrayWrapperOfPostResponse fetch_feeds_using_get2(authorization, feed_id, version, limit=limit, ref=ref)

fetchFeeds

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
ref = 'ref_example' # str | ref (optional)

try:
    # fetchFeeds
    api_response = api_instance.fetch_feeds_using_get2(authorization, feed_id, version, limit=limit, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->fetch_feeds_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfPostResponse**](ArrayWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_using_post2**
> Wrapper follow_using_post2(authorization, feed_id, version)

follow

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version

try:
    # follow
    api_response = api_instance.follow_using_post2(authorization, feed_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->follow_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_following_info_using_get**
> SingleWrapperOfFollowingInfo get_following_info_using_get(authorization, feed_id, version)

getFollowingInfo

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version

try:
    # getFollowingInfo
    api_response = api_instance.get_following_info_using_get(authorization, feed_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->get_following_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfFollowingInfo**](SingleWrapperOfFollowingInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_followers_using_get**
> ArrayWrapperOfActivityUser get_list_followers_using_get(authorization, feed_id, version, limit=limit, offset=offset)

getListFollowers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)

try:
    # getListFollowers
    api_response = api_instance.get_list_followers_using_get(authorization, feed_id, version, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->get_list_followers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**ArrayWrapperOfActivityUser**](ArrayWrapperOfActivityUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_followings_using_get**
> ArrayWrapperOfActivityUser get_list_followings_using_get(authorization, feed_id, version, limit=limit, offset=offset)

getListFollowings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)

try:
    # getListFollowings
    api_response = api_instance.get_list_followings_using_get(authorization, feed_id, version, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->get_list_followings_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**ArrayWrapperOfActivityUser**](ArrayWrapperOfActivityUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_detail_using_get1**
> SingleWrapperOfPostResponse get_post_detail_using_get1(authorization, feed_id, post_id, version)

getPostDetail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version

try:
    # getPostDetail
    api_response = api_instance.get_post_detail_using_get1(authorization, feed_id, post_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->get_post_detail_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_suggestion_using_get1**
> SingleWrapperOfPageOfUserSuggestion get_user_suggestion_using_get1(authorization, feed_id, version, limit=limit, offset=offset)

getUserSuggestion

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)

try:
    # getUserSuggestion
    api_response = api_instance.get_user_suggestion_using_get1(authorization, feed_id, version, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->get_user_suggestion_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfUserSuggestion**](SingleWrapperOfPageOfUserSuggestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react_using_post2**
> SingleWrapperOfReaction react_using_post2(body, authorization, feed_id, post_id, version)

react

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
body = dupr_backend.ReactRequest() # ReactRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version

try:
    # react
    api_response = api_instance.react_using_post2(body, authorization, feed_id, post_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->react_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReactRequest**](ReactRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfReaction**](SingleWrapperOfReaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_using_get1**
> ArrayWrapperOfReaction reactions_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)

reactions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
ref = 'ref_example' # str | ref (optional)

try:
    # reactions
    api_response = api_instance.reactions_using_get1(authorization, feed_id, post_id, version, limit=limit, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->reactions_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfReaction**](ArrayWrapperOfReaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_post_using_delete1**
> SingleWrapperOfUnit remove_post_using_delete1(authorization, feed_id, post_id, version)

removePost

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version

try:
    # removePost
    api_response = api_instance.remove_post_using_delete1(authorization, feed_id, post_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->remove_post_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeline_using_get**
> ArrayWrapperOfPostResponse timeline_using_get(authorization, feed_id, version, limit=limit, ref=ref)

timeline

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
ref = 'ref_example' # str | ref (optional)

try:
    # timeline
    api_response = api_instance.timeline_using_get(authorization, feed_id, version, limit=limit, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->timeline_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfPostResponse**](ArrayWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_using_delete2**
> Wrapper unfollow_using_delete2(authorization, feed_id, version)

unfollow

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
version = 'version_example' # str | version

try:
    # unfollow
    api_response = api_instance.unfollow_using_delete2(authorization, feed_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->unfollow_using_delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment_using_put1**
> Wrapper update_comment_using_put1(body, authorization, feed_id, post_id, version)

updateComment

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityNewsfeedsForUserApi()
body = dupr_backend.ReactRequest() # ReactRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
feed_id = 789 # int | The user's feed Id
post_id = 'post_id_example' # str | The post Id
version = 'version_example' # str | version

try:
    # updateComment
    api_response = api_instance.update_comment_using_put1(body, authorization, feed_id, post_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityNewsfeedsForUserApi->update_comment_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReactRequest**](ReactRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **feed_id** | **int**| The user&#x27;s feed Id | 
 **post_id** | **str**| The post Id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

