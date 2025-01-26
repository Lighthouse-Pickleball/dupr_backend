# dupr_backend.PaymentApi

All URIs are relative to *//https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PaymentApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # clubPaymentDashboard
    api_response = api_instance.club_payment_dashboard_using_get(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->club_payment_dashboard_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfAccountLinkResponse**](SingleWrapperOfAccountLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_payment_status_using_get**
> SingleWrapperOfAccountStatusResponse club_payment_status_using_get(authorization, club_id, version)

clubPaymentStatus

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PaymentApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # clubPaymentStatus
    api_response = api_instance.club_payment_status_using_get(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->club_payment_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfAccountStatusResponse**](SingleWrapperOfAccountStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_setup_payment_using_get**
> SingleWrapperOfAccountLinkResponse club_setup_payment_using_get(authorization, club_id, version)

clubSetupPayment

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PaymentApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # clubSetupPayment
    api_response = api_instance.club_setup_payment_using_get(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->club_setup_payment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfAccountLinkResponse**](SingleWrapperOfAccountLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

