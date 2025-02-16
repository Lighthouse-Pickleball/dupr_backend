# dupr_backend.PostReportApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reports_using_get**](PostReportApi.md#get_reports_using_get) | **GET** /report/{version}/{status} | getReports
[**report_activity_using_post**](PostReportApi.md#report_activity_using_post) | **POST** /report/{version} | reportActivity
[**report_process_using_post**](PostReportApi.md#report_process_using_post) | **POST** /report/{version}/process/{reportId}/{status} | reportProcess


# **get_reports_using_get**
> SingleWrapperOfPageOfPostReport get_reports_using_get(authorization, status, version, from_date=from_date, limit=limit, offset=offset, reason=reason, sort_by=sort_by, sort_direction=sort_direction, to_date=to_date)

getReports

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_post_report import SingleWrapperOfPageOfPostReport
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
    api_instance = dupr_backend.PostReportApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    status = 'status_example' # str | PostReport status
    version = 'v1.0' # str | version (default to 'v1.0')
    from_date = 'from_date_example' # str | fromDate (optional)
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)
    reason = 'reason_example' # str | reason (optional)
    sort_by = 'created_at' # str | sortBy (optional) (default to 'created_at')
    sort_direction = 'DESC' # str | sortDirection (optional) (default to 'DESC')
    to_date = 'to_date_example' # str | toDate (optional)

    try:
        # getReports
        api_response = api_instance.get_reports_using_get(authorization, status, version, from_date=from_date, limit=limit, offset=offset, reason=reason, sort_by=sort_by, sort_direction=sort_direction, to_date=to_date)
        print("The response of PostReportApi->get_reports_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostReportApi->get_reports_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **status** | **str**| PostReport status | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **from_date** | **str**| fromDate | [optional] 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]
 **reason** | **str**| reason | [optional] 
 **sort_by** | **str**| sortBy | [optional] [default to &#39;created_at&#39;]
 **sort_direction** | **str**| sortDirection | [optional] [default to &#39;DESC&#39;]
 **to_date** | **str**| toDate | [optional] 

### Return type

[**SingleWrapperOfPageOfPostReport**](SingleWrapperOfPageOfPostReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_activity_using_post**
> SingleWrapperOfPostReport report_activity_using_post(authorization, version, report_request)

reportActivity

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.report_request import ReportRequest
from dupr_backend.models.single_wrapper_of_post_report import SingleWrapperOfPostReport
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
    api_instance = dupr_backend.PostReportApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    report_request = dupr_backend.ReportRequest() # ReportRequest | reportRequest

    try:
        # reportActivity
        api_response = api_instance.report_activity_using_post(authorization, version, report_request)
        print("The response of PostReportApi->report_activity_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostReportApi->report_activity_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **report_request** | [**ReportRequest**](ReportRequest.md)| reportRequest | 

### Return type

[**SingleWrapperOfPostReport**](SingleWrapperOfPostReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_process_using_post**
> Wrapper report_process_using_post(authorization, report_id, status, version)

reportProcess

### Example

```python
import time
import os
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
    api_instance = dupr_backend.PostReportApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    report_id = 'report_id_example' # str | The report's Id
    status = 'status_example' # str | APPROVE/REJECT
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # reportProcess
        api_response = api_instance.report_process_using_post(authorization, report_id, status, version)
        print("The response of PostReportApi->report_process_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostReportApi->report_process_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **report_id** | **str**| The report&#39;s Id | 
 **status** | **str**| APPROVE/REJECT | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

