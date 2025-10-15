# dupr_backend.PostReportApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reports**](PostReportApi.md#get_reports) | **GET** /report/{version}/{status} | 
[**report_activity**](PostReportApi.md#report_activity) | **POST** /report/{version} | 
[**report_process**](PostReportApi.md#report_process) | **POST** /report/{version}/process/{reportId}/{status} | 


# **get_reports**
> SingleWrapperPagePostReport get_reports(version, status, limit=limit, offset=offset, from_date=from_date, to_date=to_date, reason=reason, sort_by=sort_by, sort_direction=sort_direction)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_post_report import SingleWrapperPagePostReport
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
    api_instance = dupr_backend.PostReportApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    status = 'status_example' # str | PostReport status
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    from_date = 'from_date_example' # str |  (optional)
    to_date = 'to_date_example' # str |  (optional)
    reason = 'reason_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        api_response = api_instance.get_reports(version, status, limit=limit, offset=offset, from_date=from_date, to_date=to_date, reason=reason, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of PostReportApi->get_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostReportApi->get_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **status** | **str**| PostReport status | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **from_date** | **str**|  | [optional] 
 **to_date** | **str**|  | [optional] 
 **reason** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

### Return type

[**SingleWrapperPagePostReport**](SingleWrapperPagePostReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_activity**
> SingleWrapperPostReport report_activity(version, report_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.report_request import ReportRequest
from dupr_backend.models.single_wrapper_post_report import SingleWrapperPostReport
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
    api_instance = dupr_backend.PostReportApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    report_request = dupr_backend.ReportRequest() # ReportRequest | 

    try:
        api_response = api_instance.report_activity(version, report_request)
        print("The response of PostReportApi->report_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostReportApi->report_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **report_request** | [**ReportRequest**](ReportRequest.md)|  | 

### Return type

[**SingleWrapperPostReport**](SingleWrapperPostReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_process**
> Wrapper report_process(version, report_id, status)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.PostReportApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    report_id = 'report_id_example' # str | The report's Id
    status = 'status_example' # str | APPROVE/REJECT

    try:
        api_response = api_instance.report_process(version, report_id, status)
        print("The response of PostReportApi->report_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostReportApi->report_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **report_id** | **str**| The report&#39;s Id | 
 **status** | **str**| APPROVE/REJECT | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

