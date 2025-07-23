# dupr_backend.SubscriptionsControllerApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout_session**](SubscriptionsControllerApi.md#create_checkout_session) | **PUT** /subscription/checkout/session | 
[**create_customer_portal_session**](SubscriptionsControllerApi.md#create_customer_portal_session) | **POST** /subscription/manage | 
[**get_customer_status**](SubscriptionsControllerApi.md#get_customer_status) | **GET** /subscription | 
[**get_session_payment_status**](SubscriptionsControllerApi.md#get_session_payment_status) | **POST** /subscription/checkout/session/status | 
[**get_subscriptions**](SubscriptionsControllerApi.md#get_subscriptions) | **POST** /subscription/active | 
[**track_successful_payment**](SubscriptionsControllerApi.md#track_successful_payment) | **POST** /subscription/track | 


# **create_checkout_session**
> object create_checkout_session(create_stripe_session_request)

### Example


```python
import dupr_backend
from dupr_backend.models.create_stripe_session_request import CreateStripeSessionRequest
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
    api_instance = dupr_backend.SubscriptionsControllerApi(api_client)
    create_stripe_session_request = dupr_backend.CreateStripeSessionRequest() # CreateStripeSessionRequest | 

    try:
        api_response = api_instance.create_checkout_session(create_stripe_session_request)
        print("The response of SubscriptionsControllerApi->create_checkout_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->create_checkout_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stripe_session_request** | [**CreateStripeSessionRequest**](CreateStripeSessionRequest.md)|  | 

### Return type

**object**

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

# **create_customer_portal_session**
> object create_customer_portal_session()

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.SubscriptionsControllerApi(api_client)

    try:
        api_response = api_instance.create_customer_portal_session()
        print("The response of SubscriptionsControllerApi->create_customer_portal_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->create_customer_portal_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **get_customer_status**
> object get_customer_status()

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.SubscriptionsControllerApi(api_client)

    try:
        api_response = api_instance.get_customer_status()
        print("The response of SubscriptionsControllerApi->get_customer_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->get_customer_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **get_session_payment_status**
> object get_session_payment_status(get_stripe_session_request)

### Example


```python
import dupr_backend
from dupr_backend.models.get_stripe_session_request import GetStripeSessionRequest
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
    api_instance = dupr_backend.SubscriptionsControllerApi(api_client)
    get_stripe_session_request = dupr_backend.GetStripeSessionRequest() # GetStripeSessionRequest | 

    try:
        api_response = api_instance.get_session_payment_status(get_stripe_session_request)
        print("The response of SubscriptionsControllerApi->get_session_payment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->get_session_payment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_stripe_session_request** | [**GetStripeSessionRequest**](GetStripeSessionRequest.md)|  | 

### Return type

**object**

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

# **get_subscriptions**
> object get_subscriptions()

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.SubscriptionsControllerApi(api_client)

    try:
        api_response = api_instance.get_subscriptions()
        print("The response of SubscriptionsControllerApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->get_subscriptions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **track_successful_payment**
> object track_successful_payment(request)

### Example


```python
import dupr_backend
from dupr_backend.models.payment_report_request import PaymentReportRequest
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
    api_instance = dupr_backend.SubscriptionsControllerApi(api_client)
    request = dupr_backend.PaymentReportRequest() # PaymentReportRequest | 

    try:
        api_response = api_instance.track_successful_payment(request)
        print("The response of SubscriptionsControllerApi->track_successful_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->track_successful_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PaymentReportRequest**](.md)|  | 

### Return type

**object**

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

