# dupr_backend.ActivityAdminNewsfeedsFeaturesApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_suggestions**](ActivityAdminNewsfeedsFeaturesApi.md#add_user_suggestions) | **POST** /activity/{version}/admin/user-suggestion | 
[**create_post2**](ActivityAdminNewsfeedsFeaturesApi.md#create_post2) | **POST** /activity/{version}/admin/test | 
[**fetch_feeds2**](ActivityAdminNewsfeedsFeaturesApi.md#fetch_feeds2) | **GET** /activity/{version}/admin/test | 
[**follow2**](ActivityAdminNewsfeedsFeaturesApi.md#follow2) | **POST** /activity/{version}/admin/test/follow | 
[**get_user_suggestion**](ActivityAdminNewsfeedsFeaturesApi.md#get_user_suggestion) | **GET** /activity/{version}/admin/user-suggestion | 
[**react2**](ActivityAdminNewsfeedsFeaturesApi.md#react2) | **POST** /activity/{version}/admin/test/react | 
[**remove_user_suggestions**](ActivityAdminNewsfeedsFeaturesApi.md#remove_user_suggestions) | **DELETE** /activity/{version}/admin/user-suggestion | 
[**sync_club_followers**](ActivityAdminNewsfeedsFeaturesApi.md#sync_club_followers) | **POST** /activity/{version}/admin/utils/sync/clubFollowers | 
[**sync_feeds**](ActivityAdminNewsfeedsFeaturesApi.md#sync_feeds) | **POST** /activity/{version}/admin/utils/sync | 
[**unfollow2**](ActivityAdminNewsfeedsFeaturesApi.md#unfollow2) | **DELETE** /activity/{version}/admin/test/follow | 
[**unfollow_clubs_with_same_ids**](ActivityAdminNewsfeedsFeaturesApi.md#unfollow_clubs_with_same_ids) | **POST** /activity/{version}/admin/utils/club-followers/same-id | 


# **add_user_suggestions**
> SingleWrapperUnit add_user_suggestions(version, user_suggestion_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.models.user_suggestion_request import UserSuggestionRequest
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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_suggestion_request = dupr_backend.UserSuggestionRequest() # UserSuggestionRequest | 

    try:
        api_response = api_instance.add_user_suggestions(version, user_suggestion_request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->add_user_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->add_user_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_suggestion_request** | [**UserSuggestionRequest**](UserSuggestionRequest.md)|  | 

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

# **create_post2**
> SingleWrapperPostResponse create_post2(version, slug, id, post_request)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    slug = 'slug_example' # str | 
    id = 56 # int | 
    post_request = dupr_backend.PostRequest() # PostRequest | 

    try:
        api_response = api_instance.create_post2(version, slug, id, post_request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->create_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->create_post2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **slug** | **str**|  | 
 **id** | **int**|  | 
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

# **fetch_feeds2**
> ArrayWrapperPostResponse fetch_feeds2(version, slug, id, limit=limit, ref=ref)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    slug = 'slug_example' # str | 
    id = 56 # int | 
    limit = 56 # int |  (optional)
    ref = 'ref_example' # str |  (optional)

    try:
        api_response = api_instance.fetch_feeds2(version, slug, id, limit=limit, ref=ref)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->fetch_feeds2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->fetch_feeds2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **slug** | **str**|  | 
 **id** | **int**|  | 
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

# **follow2**
> Wrapper follow2(version, followee, followee_type, follower)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    followee = 56 # int | 
    followee_type = 'followee_type_example' # str | 
    follower = 56 # int | 

    try:
        api_response = api_instance.follow2(version, followee, followee_type, follower)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->follow2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->follow2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **followee** | **int**|  | 
 **followee_type** | **str**|  | 
 **follower** | **int**|  | 

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

# **get_user_suggestion**
> SingleWrapperPageUserSuggestion get_user_suggestion(version, limit=limit, offset=offset)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    limit = 10 # int |  (optional) (default to 10)
    offset = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.get_user_suggestion(version, limit=limit, offset=offset)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->get_user_suggestion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->get_user_suggestion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 0]

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

# **react2**
> SingleWrapperReaction react2(version, actor, react_request)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    actor = 56 # int | 
    react_request = dupr_backend.ReactRequest() # ReactRequest | 

    try:
        api_response = api_instance.react2(version, actor, react_request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->react2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->react2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **actor** | **int**|  | 
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

# **remove_user_suggestions**
> SingleWrapperUnit remove_user_suggestions(version, user_suggestion_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.models.user_suggestion_request import UserSuggestionRequest
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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_suggestion_request = dupr_backend.UserSuggestionRequest() # UserSuggestionRequest | 

    try:
        api_response = api_instance.remove_user_suggestions(version, user_suggestion_request)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->remove_user_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->remove_user_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_suggestion_request** | [**UserSuggestionRequest**](UserSuggestionRequest.md)|  | 

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

# **sync_club_followers**
> SingleWrapperUnit sync_club_followers(version, batch_size, delay, offset=offset)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    batch_size = 56 # int | 
    delay = 56 # int | 
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.sync_club_followers(version, batch_size, delay, offset=offset)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->sync_club_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->sync_club_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **batch_size** | **int**|  | 
 **delay** | **int**|  | 
 **offset** | **int**|  | [optional] 

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

# **sync_feeds**
> SingleWrapperUnit sync_feeds(version, slug, id)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    slug = 'slug_example' # str | 
    id = 56 # int | 

    try:
        api_response = api_instance.sync_feeds(version, slug, id)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->sync_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->sync_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **slug** | **str**|  | 
 **id** | **int**|  | 

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

# **unfollow2**
> Wrapper unfollow2(version, followee, followee_type, follower)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    followee = 56 # int | 
    followee_type = 'followee_type_example' # str | 
    follower = 56 # int | 

    try:
        api_response = api_instance.unfollow2(version, followee, followee_type, follower)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->unfollow2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->unfollow2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **followee** | **int**|  | 
 **followee_type** | **str**|  | 
 **follower** | **int**|  | 

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

# **unfollow_clubs_with_same_ids**
> SingleWrapperUnit unfollow_clubs_with_same_ids(version, offset)

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
    api_instance = dupr_backend.ActivityAdminNewsfeedsFeaturesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    offset = 56 # int | 

    try:
        api_response = api_instance.unfollow_clubs_with_same_ids(version, offset)
        print("The response of ActivityAdminNewsfeedsFeaturesApi->unfollow_clubs_with_same_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityAdminNewsfeedsFeaturesApi->unfollow_clubs_with_same_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **offset** | **int**|  | 

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

