# dupr_backend.UserSubscriptionsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_subscriptions**](UserSubscriptionsApi.md#add_user_subscriptions) | **POST** /admin/user-subscriptions | 
[**get_all_user_subscriptions**](UserSubscriptionsApi.md#get_all_user_subscriptions) | **GET** /admin/user-subscriptions | 
[**remove_user_subscriptions**](UserSubscriptionsApi.md#remove_user_subscriptions) | **DELETE** /admin/user-subscriptions/{id} | 
[**update_user_subscriptions**](UserSubscriptionsApi.md#update_user_subscriptions) | **PUT** /admin/user-subscriptions/{id} | 


# **add_user_subscriptions**
> SingleWrapperUnit add_user_subscriptions(user_subscription_request)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.models.user_subscription_request import UserSubscriptionRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    user_subscription_request = dupr_backend.UserSubscriptionRequest() # UserSubscriptionRequest | 

    try:
        api_response = api_instance.add_user_subscriptions(user_subscription_request)
        print("The response of UserSubscriptionsApi->add_user_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->add_user_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_subscription_request** | [**UserSubscriptionRequest**](UserSubscriptionRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_subscriptions**
> PageUserSubscription get_all_user_subscriptions(limit=limit, offset=offset)

### Example


```python
import dupr_backend
from dupr_backend.models.page_user_subscription import PageUserSubscription
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.get_all_user_subscriptions(limit=limit, offset=offset)
        print("The response of UserSubscriptionsApi->get_all_user_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->get_all_user_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**PageUserSubscription**](PageUserSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_subscriptions**
> SingleWrapperUnit remove_user_subscriptions(id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.remove_user_subscriptions(id)
        print("The response of UserSubscriptionsApi->remove_user_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->remove_user_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_subscriptions**
> SingleWrapperUnit update_user_subscriptions(id, user_subscription_request)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.models.user_subscription_request import UserSubscriptionRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    id = 56 # int | 
    user_subscription_request = dupr_backend.UserSubscriptionRequest() # UserSubscriptionRequest | 

    try:
        api_response = api_instance.update_user_subscriptions(id, user_subscription_request)
        print("The response of UserSubscriptionsApi->update_user_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->update_user_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **user_subscription_request** | [**UserSubscriptionRequest**](UserSubscriptionRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

