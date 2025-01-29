# dupr_backend.ActivityAdminNewsfeedsFeaturesApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_suggestions_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#add_user_suggestions_using_post) | **POST** /activity/{version}/admin/user-suggestion | addUserSuggestions
[**create_post_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#create_post_using_post) | **POST** /activity/{version}/admin/test | createPost
[**fetch_feeds_using_get**](ActivityAdminNewsfeedsFeaturesApi.md#fetch_feeds_using_get) | **GET** /activity/{version}/admin/test | fetchFeeds
[**follow_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#follow_using_post) | **POST** /activity/{version}/admin/test/follow | follow
[**get_user_suggestion_using_get**](ActivityAdminNewsfeedsFeaturesApi.md#get_user_suggestion_using_get) | **GET** /activity/{version}/admin/user-suggestion | getUserSuggestion
[**react_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#react_using_post) | **POST** /activity/{version}/admin/test/react | react
[**remove_user_suggestions_using_delete**](ActivityAdminNewsfeedsFeaturesApi.md#remove_user_suggestions_using_delete) | **DELETE** /activity/{version}/admin/user-suggestion | removeUserSuggestions
[**sync_club_followers_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#sync_club_followers_using_post) | **POST** /activity/{version}/admin/utils/sync/clubFollowers | syncClubFollowers
[**sync_feeds_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#sync_feeds_using_post) | **POST** /activity/{version}/admin/utils/sync | syncFeeds
[**unfollow_clubs_with_same_ids_using_post**](ActivityAdminNewsfeedsFeaturesApi.md#unfollow_clubs_with_same_ids_using_post) | **POST** /activity/{version}/admin/utils/club-followers/same-id | unfollowClubsWithSameIds
[**unfollow_using_delete**](ActivityAdminNewsfeedsFeaturesApi.md#unfollow_using_delete) | **DELETE** /activity/{version}/admin/test/follow | unfollow

# **add_user_suggestions_using_post**
> SingleWrapperOfUnit add_user_suggestions_using_post(body, authorization, version)

addUserSuggestions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
body = dupr_backend.UserSuggestionRequest() # UserSuggestionRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # addUserSuggestions
    api_response = api_instance.add_user_suggestions_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->add_user_suggestions_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSuggestionRequest**](UserSuggestionRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_post_using_post**
> SingleWrapperOfPostResponse create_post_using_post(body, authorization, id, slug, version)

createPost

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
body = dupr_backend.PostRequest() # PostRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
slug = 'slug_example' # str | slug
version = 'version_example' # str | version

try:
    # createPost
    api_response = api_instance.create_post_using_post(body, authorization, id, slug, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->create_post_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRequest**](PostRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **slug** | **str**| slug | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feeds_using_get**
> ArrayWrapperOfPostResponse fetch_feeds_using_get(authorization, id, slug, version, limit=limit, ref=ref)

fetchFeeds

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
slug = 'slug_example' # str | slug
version = 'version_example' # str | version
limit = 56 # int | limit (optional)
ref = 'ref_example' # str | ref (optional)

try:
    # fetchFeeds
    api_response = api_instance.fetch_feeds_using_get(authorization, id, slug, version, limit=limit, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->fetch_feeds_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **slug** | **str**| slug | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] 
 **ref** | **str**| ref | [optional] 

### Return type

[**ArrayWrapperOfPostResponse**](ArrayWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_using_post**
> Wrapper follow_using_post(authorization, followee, followee_type, follower, version)

follow

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
followee = 789 # int | followee
followee_type = 'followee_type_example' # str | followeeType
follower = 789 # int | follower
version = 'version_example' # str | version

try:
    # follow
    api_response = api_instance.follow_using_post(authorization, followee, followee_type, follower, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->follow_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **followee** | **int**| followee | 
 **followee_type** | **str**| followeeType | 
 **follower** | **int**| follower | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_suggestion_using_get**
> SingleWrapperOfPageOfUserSuggestion get_user_suggestion_using_get(authorization, version, limit=limit, offset=offset)

getUserSuggestion

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)

try:
    # getUserSuggestion
    api_response = api_instance.get_user_suggestion_using_get(authorization, version, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->get_user_suggestion_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
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

# **react_using_post**
> SingleWrapperOfReaction react_using_post(body, authorization, actor, version)

react

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
body = dupr_backend.ReactRequest() # ReactRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
actor = 789 # int | actor
version = 'version_example' # str | version

try:
    # react
    api_response = api_instance.react_using_post(body, authorization, actor, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->react_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReactRequest**](ReactRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **actor** | **int**| actor | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfReaction**](SingleWrapperOfReaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_suggestions_using_delete**
> SingleWrapperOfUnit remove_user_suggestions_using_delete(body, authorization, version)

removeUserSuggestions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
body = dupr_backend.UserSuggestionRequest() # UserSuggestionRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # removeUserSuggestions
    api_response = api_instance.remove_user_suggestions_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->remove_user_suggestions_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSuggestionRequest**](UserSuggestionRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_club_followers_using_post**
> SingleWrapperOfUnit sync_club_followers_using_post(authorization, batch_size, delay, version, offset=offset)

syncClubFollowers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
batch_size = 56 # int | batchSize
delay = 56 # int | delay
version = 'version_example' # str | version
offset = 789 # int | offset (optional)

try:
    # syncClubFollowers
    api_response = api_instance.sync_club_followers_using_post(authorization, batch_size, delay, version, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->sync_club_followers_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **batch_size** | **int**| batchSize | 
 **delay** | **int**| delay | 
 **version** | **str**| version | 
 **offset** | **int**| offset | [optional] 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_feeds_using_post**
> SingleWrapperOfUnit sync_feeds_using_post(authorization, id, slug, version)

syncFeeds

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
slug = 'slug_example' # str | slug
version = 'version_example' # str | version

try:
    # syncFeeds
    api_response = api_instance.sync_feeds_using_post(authorization, id, slug, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->sync_feeds_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **slug** | **str**| slug | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_clubs_with_same_ids_using_post**
> SingleWrapperOfUnit unfollow_clubs_with_same_ids_using_post(authorization, offset, version)

unfollowClubsWithSameIds

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # unfollowClubsWithSameIds
    api_response = api_instance.unfollow_clubs_with_same_ids_using_post(authorization, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->unfollow_clubs_with_same_ids_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_using_delete**
> Wrapper unfollow_using_delete(authorization, followee, followee_type, follower, version)

unfollow

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
followee = 789 # int | followee
followee_type = 'followee_type_example' # str | followeeType
follower = 789 # int | follower
version = 'version_example' # str | version

try:
    # unfollow
    api_response = api_instance.unfollow_using_delete(authorization, followee, followee_type, follower, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->unfollow_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **followee** | **int**| followee | 
 **followee_type** | **str**| followeeType | 
 **follower** | **int**| follower | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

