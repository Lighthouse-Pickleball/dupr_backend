# dupr_backend.ActivityAdminNewsfeedsFeaturesApi

All URIs are relative to *http://https://backend.mydupr.com*

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
> SingleWrapperOfUnit add_user_suggestions_using_post(authorization, version, request)

addUserSuggestions

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
from dupr_backend.models.user_suggestion_request import UserSuggestionRequest
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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserSuggestionRequest() # UserSuggestionRequest | request

    try:
        # addUserSuggestions
        api_response = api_instance.add_user_suggestions_using_post(authorization, version, request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->add_user_suggestions_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->add_user_suggestions_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserSuggestionRequest**](UserSuggestionRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **create_post_using_post**
> SingleWrapperOfPostResponse create_post_using_post(authorization, id, slug, version, request)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    slug = 'slug_example' # str | slug
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PostRequest() # PostRequest | request

    try:
        # createPost
        api_response = api_instance.create_post_using_post(authorization, id, slug, version, request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->create_post_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->create_post_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **slug** | **str**| slug | 
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

# **fetch_feeds_using_get**
> ArrayWrapperOfPostResponse fetch_feeds_using_get(authorization, id, slug, version, limit=limit, ref=ref)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    slug = 'slug_example' # str | slug
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 56 # int | limit (optional)
    ref = 'ref_example' # str | ref (optional)

    try:
        # fetchFeeds
        api_response = api_instance.fetch_feeds_using_get(authorization, id, slug, version, limit=limit, ref=ref)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->fetch_feeds_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->fetch_feeds_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **slug** | **str**| slug | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] 
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

# **follow_using_post**
> Wrapper follow_using_post(authorization, followee, followee_type, follower, version)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    followee = 56 # int | followee
    followee_type = 'followee_type_example' # str | followeeType
    follower = 56 # int | follower
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # follow
        api_response = api_instance.follow_using_post(authorization, followee, followee_type, follower, version)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->follow_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->follow_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **followee** | **int**| followee | 
 **followee_type** | **str**| followeeType | 
 **follower** | **int**| follower | 
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

# **get_user_suggestion_using_get**
> SingleWrapperOfPageOfUserSuggestion get_user_suggestion_using_get(authorization, version, limit=limit, offset=offset)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)

    try:
        # getUserSuggestion
        api_response = api_instance.get_user_suggestion_using_get(authorization, version, limit=limit, offset=offset)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->get_user_suggestion_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->get_user_suggestion_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **react_using_post**
> SingleWrapperOfReaction react_using_post(actor, authorization, version, request)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    actor = 56 # int | actor
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ReactRequest() # ReactRequest | request

    try:
        # react
        api_response = api_instance.react_using_post(actor, authorization, version, request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->react_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->react_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor** | **int**| actor | 
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **remove_user_suggestions_using_delete**
> SingleWrapperOfUnit remove_user_suggestions_using_delete(authorization, version, request)

removeUserSuggestions

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
from dupr_backend.models.user_suggestion_request import UserSuggestionRequest
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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserSuggestionRequest() # UserSuggestionRequest | request

    try:
        # removeUserSuggestions
        api_response = api_instance.remove_user_suggestions_using_delete(authorization, version, request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->remove_user_suggestions_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->remove_user_suggestions_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserSuggestionRequest**](UserSuggestionRequest.md)| request | 

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

# **sync_club_followers_using_post**
> SingleWrapperOfUnit sync_club_followers_using_post(authorization, batch_size, delay, version, offset=offset)

syncClubFollowers

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    batch_size = 56 # int | batchSize
    delay = 56 # int | delay
    version = 'v1.0' # str | version (default to 'v1.0')
    offset = 56 # int | offset (optional)

    try:
        # syncClubFollowers
        api_response = api_instance.sync_club_followers_using_post(authorization, batch_size, delay, version, offset=offset)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->sync_club_followers_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->sync_club_followers_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **batch_size** | **int**| batchSize | 
 **delay** | **int**| delay | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **offset** | **int**| offset | [optional] 

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

# **sync_feeds_using_post**
> SingleWrapperOfUnit sync_feeds_using_post(authorization, id, slug, version)

syncFeeds

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    slug = 'slug_example' # str | slug
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # syncFeeds
        api_response = api_instance.sync_feeds_using_post(authorization, id, slug, version)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->sync_feeds_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->sync_feeds_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **slug** | **str**| slug | 
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

# **unfollow_clubs_with_same_ids_using_post**
> SingleWrapperOfUnit unfollow_clubs_with_same_ids_using_post(authorization, offset, version)

unfollowClubsWithSameIds

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # unfollowClubsWithSameIds
        api_response = api_instance.unfollow_clubs_with_same_ids_using_post(authorization, offset, version)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->unfollow_clubs_with_same_ids_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->unfollow_clubs_with_same_ids_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **offset** | **int**| offset | 
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

# **unfollow_using_delete**
> Wrapper unfollow_using_delete(authorization, followee, followee_type, follower, version)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    followee = 56 # int | followee
    followee_type = 'followee_type_example' # str | followeeType
    follower = 56 # int | follower
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # unfollow
        api_response = api_instance.unfollow_using_delete(authorization, followee, followee_type, follower, version)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->unfollow_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->unfollow_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **followee** | **int**| followee | 
 **followee_type** | **str**| followeeType | 
 **follower** | **int**| follower | 
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

