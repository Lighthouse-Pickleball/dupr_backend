# dupr_backend.StripeApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_charge_updates**](StripeApi.md#account_charge_updates) | **POST** /stripe/account/{version}/charge | 
[**account_checkout_updates**](StripeApi.md#account_checkout_updates) | **POST** /stripe/account/{version}/checkout | 
[**charge_updates**](StripeApi.md#charge_updates) | **POST** /stripe/{version}/charge | 
[**checkout_account_payment_intent**](StripeApi.md#checkout_account_payment_intent) | **POST** /stripe/account/{version}/payment-intent | 
[**checkout_payment_intent**](StripeApi.md#checkout_payment_intent) | **POST** /stripe/{version}/payment-intent | 
[**checkout_updates**](StripeApi.md#checkout_updates) | **POST** /stripe/{version}/checkout | 
[**club_account_updates**](StripeApi.md#club_account_updates) | **POST** /stripe/account/{version}/updated | 
[**invoice_updates**](StripeApi.md#invoice_updates) | **POST** /stripe/{version}/invoices | 
[**subscription_updates**](StripeApi.md#subscription_updates) | **POST** /stripe/{version}/subscriptions | 


# **account_charge_updates**
> object account_charge_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.account_charge_updates(version, stripe_signature, body)
        print("The response of StripeApi->account_charge_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->account_charge_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **account_checkout_updates**
> object account_checkout_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.account_checkout_updates(version, stripe_signature, body)
        print("The response of StripeApi->account_checkout_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->account_checkout_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **charge_updates**
> object charge_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.charge_updates(version, stripe_signature, body)
        print("The response of StripeApi->charge_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->charge_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **checkout_account_payment_intent**
> object checkout_account_payment_intent(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.checkout_account_payment_intent(version, stripe_signature, body)
        print("The response of StripeApi->checkout_account_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->checkout_account_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **checkout_payment_intent**
> object checkout_payment_intent(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.checkout_payment_intent(version, stripe_signature, body)
        print("The response of StripeApi->checkout_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->checkout_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **checkout_updates**
> object checkout_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.checkout_updates(version, stripe_signature, body)
        print("The response of StripeApi->checkout_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->checkout_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **club_account_updates**
> object club_account_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.club_account_updates(version, stripe_signature, body)
        print("The response of StripeApi->club_account_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->club_account_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **invoice_updates**
> object invoice_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.invoice_updates(version, stripe_signature, body)
        print("The response of StripeApi->invoice_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->invoice_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

# **subscription_updates**
> object subscription_updates(version, stripe_signature, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.StripeApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    stripe_signature = 'stripe_signature_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.subscription_updates(version, stripe_signature, body)
        print("The response of StripeApi->subscription_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->subscription_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **stripe_signature** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

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

