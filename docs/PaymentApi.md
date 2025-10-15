# dupr_backend.PaymentApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**club_payment_dashboard**](PaymentApi.md#club_payment_dashboard) | **GET** /payment/club/{clubId}/{version}/dashboard | 
[**club_payment_status**](PaymentApi.md#club_payment_status) | **GET** /payment/club/{clubId}/{version}/status | 
[**club_setup_payment**](PaymentApi.md#club_setup_payment) | **GET** /payment/club/{clubId}/{version}/setup | 


# **club_payment_dashboard**
> SingleWrapperAccountLinkResponse club_payment_dashboard(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_account_link_response import SingleWrapperAccountLinkResponse
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
    api_instance = dupr_backend.PaymentApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 

    try:
        api_response = api_instance.club_payment_dashboard(version, club_id)
        print("The response of PaymentApi->club_payment_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->club_payment_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperAccountLinkResponse**](SingleWrapperAccountLinkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_payment_status**
> SingleWrapperAccountStatusResponse club_payment_status(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_account_status_response import SingleWrapperAccountStatusResponse
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
    api_instance = dupr_backend.PaymentApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 

    try:
        api_response = api_instance.club_payment_status(version, club_id)
        print("The response of PaymentApi->club_payment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->club_payment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperAccountStatusResponse**](SingleWrapperAccountStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_setup_payment**
> SingleWrapperAccountLinkResponse club_setup_payment(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_account_link_response import SingleWrapperAccountLinkResponse
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
    api_instance = dupr_backend.PaymentApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 

    try:
        api_response = api_instance.club_setup_payment(version, club_id)
        print("The response of PaymentApi->club_setup_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->club_setup_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperAccountLinkResponse**](SingleWrapperAccountLinkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

