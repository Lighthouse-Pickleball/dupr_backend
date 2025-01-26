# dupr_backend.SubscriptionsApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_using_put**](SubscriptionsApi.md#checkout_using_put) | **PUT** /subscription/{version}/{planId}/checkout | checkout
[**customer_portal_using_put**](SubscriptionsApi.md#customer_portal_using_put) | **PUT** /subscription/{version}/customer-portal | customerPortal
[**is_subscribed_using_get**](SubscriptionsApi.md#is_subscribed_using_get) | **GET** /subscription/{version}/subscribed | isSubscribed
[**subscriptions_using_get**](SubscriptionsApi.md#subscriptions_using_get) | **GET** /subscription/{version}/all | subscriptions

# **checkout_using_put**
> Wrapper checkout_using_put(authorization, plan_id, version)

checkout

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SubscriptionsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
plan_id = 789 # int | planId
version = 'version_example' # str | version

try:
    # checkout
    api_response = api_instance.checkout_using_put(authorization, plan_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->checkout_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **plan_id** | **int**| planId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_portal_using_put**
> Wrapper customer_portal_using_put(authorization, version)

customerPortal

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SubscriptionsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # customerPortal
    api_response = api_instance.customer_portal_using_put(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->customer_portal_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_subscribed_using_get**
> Wrapper is_subscribed_using_get(authorization, version)

isSubscribed

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SubscriptionsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # isSubscribed
    api_response = api_instance.is_subscribed_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->is_subscribed_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_using_get**
> Wrapper subscriptions_using_get(authorization, version)

subscriptions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SubscriptionsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # subscriptions
    api_response = api_instance.subscriptions_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

