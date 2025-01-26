# dupr_backend.UserSubscriptionsApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_subscriptions_using_post**](UserSubscriptionsApi.md#add_user_subscriptions_using_post) | **POST** /admin/user-subscriptions | addUserSubscriptions
[**get_all_user_subscriptions_using_get**](UserSubscriptionsApi.md#get_all_user_subscriptions_using_get) | **GET** /admin/user-subscriptions | getAllUserSubscriptions
[**remove_user_subscriptions_using_delete**](UserSubscriptionsApi.md#remove_user_subscriptions_using_delete) | **DELETE** /admin/user-subscriptions/{id} | removeUserSubscriptions
[**update_user_subscriptions_using_put**](UserSubscriptionsApi.md#update_user_subscriptions_using_put) | **PUT** /admin/user-subscriptions/{id} | updateUserSubscriptions

# **add_user_subscriptions_using_post**
> SingleWrapperOfUnit add_user_subscriptions_using_post(body, authorization)

addUserSubscriptions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserSubscriptionsApi()
body = dupr_backend.UserSubscriptionRequest() # UserSubscriptionRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )

try:
    # addUserSubscriptions
    api_response = api_instance.add_user_subscriptions_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubscriptionsApi->add_user_subscriptions_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSubscriptionRequest**](UserSubscriptionRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_subscriptions_using_get**
> PageOfUserSubscription get_all_user_subscriptions_using_get(authorization, limit=limit, offset=offset)

getAllUserSubscriptions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserSubscriptionsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)

try:
    # getAllUserSubscriptions
    api_response = api_instance.get_all_user_subscriptions_using_get(authorization, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubscriptionsApi->get_all_user_subscriptions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**PageOfUserSubscription**](PageOfUserSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_subscriptions_using_delete**
> SingleWrapperOfUnit remove_user_subscriptions_using_delete(authorization, id)

removeUserSubscriptions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserSubscriptionsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id

try:
    # removeUserSubscriptions
    api_response = api_instance.remove_user_subscriptions_using_delete(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubscriptionsApi->remove_user_subscriptions_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_subscriptions_using_put**
> SingleWrapperOfUnit update_user_subscriptions_using_put(body, authorization, id)

updateUserSubscriptions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserSubscriptionsApi()
body = dupr_backend.UserSubscriptionRequest() # UserSubscriptionRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id

try:
    # updateUserSubscriptions
    api_response = api_instance.update_user_subscriptions_using_put(body, authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubscriptionsApi->update_user_subscriptions_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSubscriptionRequest**](UserSubscriptionRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

