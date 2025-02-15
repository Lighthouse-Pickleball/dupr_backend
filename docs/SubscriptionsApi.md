# dupr_backend.SubscriptionsApi

All URIs are relative to *http://https://backend.mydupr.com*

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
    api_instance = dupr_backend.SubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    plan_id = 56 # int | planId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # checkout
        api_response = api_instance.checkout_using_put(authorization, plan_id, version)
        print("The response of SubscriptionsApi->checkout_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->checkout_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **plan_id** | **int**| planId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **customer_portal_using_put**
> Wrapper customer_portal_using_put(authorization, version)

customerPortal

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
    api_instance = dupr_backend.SubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # customerPortal
        api_response = api_instance.customer_portal_using_put(authorization, version)
        print("The response of SubscriptionsApi->customer_portal_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->customer_portal_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **is_subscribed_using_get**
> Wrapper is_subscribed_using_get(authorization, version)

isSubscribed

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
    api_instance = dupr_backend.SubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # isSubscribed
        api_response = api_instance.is_subscribed_using_get(authorization, version)
        print("The response of SubscriptionsApi->is_subscribed_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->is_subscribed_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **subscriptions_using_get**
> Wrapper subscriptions_using_get(authorization, version)

subscriptions

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
    api_instance = dupr_backend.SubscriptionsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # subscriptions
        api_response = api_instance.subscriptions_using_get(authorization, version)
        print("The response of SubscriptionsApi->subscriptions_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

