# dupr_backend.PaymentApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**club_payment_dashboard_using_get**](PaymentApi.md#club_payment_dashboard_using_get) | **GET** /payment/club/{clubId}/{version}/dashboard | clubPaymentDashboard
[**club_payment_status_using_get**](PaymentApi.md#club_payment_status_using_get) | **GET** /payment/club/{clubId}/{version}/status | clubPaymentStatus
[**club_setup_payment_using_get**](PaymentApi.md#club_setup_payment_using_get) | **GET** /payment/club/{clubId}/{version}/setup | clubSetupPayment


# **club_payment_dashboard_using_get**
> SingleWrapperOfAccountLinkResponse club_payment_dashboard_using_get(authorization, club_id, version)

clubPaymentDashboard

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_account_link_response import SingleWrapperOfAccountLinkResponse
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
    api_instance = dupr_backend.PaymentApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # clubPaymentDashboard
        api_response = api_instance.club_payment_dashboard_using_get(authorization, club_id, version)
        print("The response of PaymentApi->club_payment_dashboard_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->club_payment_dashboard_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfAccountLinkResponse**](SingleWrapperOfAccountLinkResponse.md)

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

# **club_payment_status_using_get**
> SingleWrapperOfAccountStatusResponse club_payment_status_using_get(authorization, club_id, version)

clubPaymentStatus

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_account_status_response import SingleWrapperOfAccountStatusResponse
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
    api_instance = dupr_backend.PaymentApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # clubPaymentStatus
        api_response = api_instance.club_payment_status_using_get(authorization, club_id, version)
        print("The response of PaymentApi->club_payment_status_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->club_payment_status_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfAccountStatusResponse**](SingleWrapperOfAccountStatusResponse.md)

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

# **club_setup_payment_using_get**
> SingleWrapperOfAccountLinkResponse club_setup_payment_using_get(authorization, club_id, version)

clubSetupPayment

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_account_link_response import SingleWrapperOfAccountLinkResponse
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
    api_instance = dupr_backend.PaymentApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # clubSetupPayment
        api_response = api_instance.club_setup_payment_using_get(authorization, club_id, version)
        print("The response of PaymentApi->club_setup_payment_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->club_setup_payment_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfAccountLinkResponse**](SingleWrapperOfAccountLinkResponse.md)

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

