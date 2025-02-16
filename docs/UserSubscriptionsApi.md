# dupr_backend.UserSubscriptionsApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_subscriptions_using_post**](UserSubscriptionsApi.md#add_user_subscriptions_using_post) | **POST** /admin/user-subscriptions | addUserSubscriptions
[**get_all_user_subscriptions_using_get**](UserSubscriptionsApi.md#get_all_user_subscriptions_using_get) | **GET** /admin/user-subscriptions | getAllUserSubscriptions
[**remove_user_subscriptions_using_delete**](UserSubscriptionsApi.md#remove_user_subscriptions_using_delete) | **DELETE** /admin/user-subscriptions/{id} | removeUserSubscriptions
[**update_user_subscriptions_using_put**](UserSubscriptionsApi.md#update_user_subscriptions_using_put) | **PUT** /admin/user-subscriptions/{id} | updateUserSubscriptions


# **add_user_subscriptions_using_post**
> SingleWrapperOfUnit add_user_subscriptions_using_post(authorization, request)

addUserSubscriptions

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
from dupr_backend.models.user_subscription_request import UserSubscriptionRequest
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
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    request = dupr_backend.UserSubscriptionRequest() # UserSubscriptionRequest | request

    try:
        # addUserSubscriptions
        api_response = api_instance.add_user_subscriptions_using_post(authorization, request)
        print("The response of UserSubscriptionsApi->add_user_subscriptions_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->add_user_subscriptions_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **request** | [**UserSubscriptionRequest**](UserSubscriptionRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **get_all_user_subscriptions_using_get**
> PageOfUserSubscription get_all_user_subscriptions_using_get(authorization, limit=limit, offset=offset)

getAllUserSubscriptions

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.page_of_user_subscription import PageOfUserSubscription
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
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)

    try:
        # getAllUserSubscriptions
        api_response = api_instance.get_all_user_subscriptions_using_get(authorization, limit=limit, offset=offset)
        print("The response of UserSubscriptionsApi->get_all_user_subscriptions_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->get_all_user_subscriptions_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**PageOfUserSubscription**](PageOfUserSubscription.md)

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

# **remove_user_subscriptions_using_delete**
> SingleWrapperOfUnit remove_user_subscriptions_using_delete(authorization, id)

removeUserSubscriptions

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
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id

    try:
        # removeUserSubscriptions
        api_response = api_instance.remove_user_subscriptions_using_delete(authorization, id)
        print("The response of UserSubscriptionsApi->remove_user_subscriptions_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->remove_user_subscriptions_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **update_user_subscriptions_using_put**
> SingleWrapperOfUnit update_user_subscriptions_using_put(authorization, id, request)

updateUserSubscriptions

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
from dupr_backend.models.user_subscription_request import UserSubscriptionRequest
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
    api_instance = dupr_backend.UserSubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    request = dupr_backend.UserSubscriptionRequest() # UserSubscriptionRequest | request

    try:
        # updateUserSubscriptions
        api_response = api_instance.update_user_subscriptions_using_put(authorization, id, request)
        print("The response of UserSubscriptionsApi->update_user_subscriptions_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionsApi->update_user_subscriptions_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **request** | [**UserSubscriptionRequest**](UserSubscriptionRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

