# dupr_backend.SubscriptionsControllerApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_portal_session**](SubscriptionsControllerApi.md#create_customer_portal_session) | **POST** /subscription/manage | 
[**get_active_products**](SubscriptionsControllerApi.md#get_active_products) | **POST** /subscription/checkout/products/active | 
[**get_customer_status**](SubscriptionsControllerApi.md#get_customer_status) | **GET** /subscription | 
[**get_session_payment_status**](SubscriptionsControllerApi.md#get_session_payment_status) | **POST** /subscription/checkout/session/status | 
[**get_subscriptions**](SubscriptionsControllerApi.md#get_subscriptions) | **POST** /subscription/active | 
[**track_successful_payment**](SubscriptionsControllerApi.md#track_successful_payment) | **POST** /subscription/track | 


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

# **get_active_products**
> ResultGetActiveProductsResponse get_active_products(get_products_for_client_key_request)

### Example


```python
import dupr_backend
from dupr_backend.models.get_products_for_client_key_request import GetProductsForClientKeyRequest
from dupr_backend.models.result_get_active_products_response import ResultGetActiveProductsResponse
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
    get_products_for_client_key_request = dupr_backend.GetProductsForClientKeyRequest() # GetProductsForClientKeyRequest | 

    try:
        api_response = api_instance.get_active_products(get_products_for_client_key_request)
        print("The response of SubscriptionsControllerApi->get_active_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsControllerApi->get_active_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_products_for_client_key_request** | [**GetProductsForClientKeyRequest**](GetProductsForClientKeyRequest.md)|  | 

### Return type

[**ResultGetActiveProductsResponse**](ResultGetActiveProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

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
> SubscriptionResponse get_subscriptions()

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.subscription_response import SubscriptionResponse
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

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Subscription objects that indicate the level of access the user has to each resource |  -  |

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

