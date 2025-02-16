# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from dupr_backend.models.single_wrapper_of_account_link_response import SingleWrapperOfAccountLinkResponse
from dupr_backend.models.single_wrapper_of_account_status_response import SingleWrapperOfAccountStatusResponse

from dupr_backend.api_client import ApiClient
from dupr_backend.api_response import ApiResponse
from dupr_backend.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PaymentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def club_payment_dashboard_using_get(self, authorization : StrictStr, club_id : Annotated[StrictInt, Field(..., description="clubId")], version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> SingleWrapperOfAccountLinkResponse:  # noqa: E501
        """clubPaymentDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.club_payment_dashboard_using_get(authorization, club_id, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param club_id: clubId (required)
        :type club_id: int
        :param version: version (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SingleWrapperOfAccountLinkResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the club_payment_dashboard_using_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.club_payment_dashboard_using_get_with_http_info(authorization, club_id, version, **kwargs)  # noqa: E501

    @validate_arguments
    def club_payment_dashboard_using_get_with_http_info(self, authorization : StrictStr, club_id : Annotated[StrictInt, Field(..., description="clubId")], version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> ApiResponse:  # noqa: E501
        """clubPaymentDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.club_payment_dashboard_using_get_with_http_info(authorization, club_id, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param club_id: clubId (required)
        :type club_id: int
        :param version: version (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SingleWrapperOfAccountLinkResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
            'club_id',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method club_payment_dashboard_using_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['club_id']:
            _path_params['clubId'] = _params['club_id']

        if _params['version']:
            _path_params['version'] = _params['version']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "SingleWrapperOfAccountLinkResponse",
            '403': None,
        }

        return self.api_client.call_api(
            '/payment/club/{clubId}/{version}/dashboard', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def club_payment_status_using_get(self, authorization : StrictStr, club_id : Annotated[StrictInt, Field(..., description="clubId")], version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> SingleWrapperOfAccountStatusResponse:  # noqa: E501
        """clubPaymentStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.club_payment_status_using_get(authorization, club_id, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param club_id: clubId (required)
        :type club_id: int
        :param version: version (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SingleWrapperOfAccountStatusResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the club_payment_status_using_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.club_payment_status_using_get_with_http_info(authorization, club_id, version, **kwargs)  # noqa: E501

    @validate_arguments
    def club_payment_status_using_get_with_http_info(self, authorization : StrictStr, club_id : Annotated[StrictInt, Field(..., description="clubId")], version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> ApiResponse:  # noqa: E501
        """clubPaymentStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.club_payment_status_using_get_with_http_info(authorization, club_id, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param club_id: clubId (required)
        :type club_id: int
        :param version: version (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SingleWrapperOfAccountStatusResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
            'club_id',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method club_payment_status_using_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['club_id']:
            _path_params['clubId'] = _params['club_id']

        if _params['version']:
            _path_params['version'] = _params['version']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "SingleWrapperOfAccountStatusResponse",
            '403': None,
        }

        return self.api_client.call_api(
            '/payment/club/{clubId}/{version}/status', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def club_setup_payment_using_get(self, authorization : StrictStr, club_id : Annotated[StrictInt, Field(..., description="clubId")], version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> SingleWrapperOfAccountLinkResponse:  # noqa: E501
        """clubSetupPayment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.club_setup_payment_using_get(authorization, club_id, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param club_id: clubId (required)
        :type club_id: int
        :param version: version (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SingleWrapperOfAccountLinkResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the club_setup_payment_using_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.club_setup_payment_using_get_with_http_info(authorization, club_id, version, **kwargs)  # noqa: E501

    @validate_arguments
    def club_setup_payment_using_get_with_http_info(self, authorization : StrictStr, club_id : Annotated[StrictInt, Field(..., description="clubId")], version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> ApiResponse:  # noqa: E501
        """clubSetupPayment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.club_setup_payment_using_get_with_http_info(authorization, club_id, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param club_id: clubId (required)
        :type club_id: int
        :param version: version (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SingleWrapperOfAccountLinkResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
            'club_id',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method club_setup_payment_using_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['club_id']:
            _path_params['clubId'] = _params['club_id']

        if _params['version']:
            _path_params['version'] = _params['version']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "SingleWrapperOfAccountLinkResponse",
            '403': None,
        }

        return self.api_client.call_api(
            '/payment/club/{clubId}/{version}/setup', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
