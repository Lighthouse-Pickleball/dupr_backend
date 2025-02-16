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

from typing import Any, Dict, Optional

from dupr_backend.models.delete_user_response import DeleteUserResponse
from dupr_backend.models.user_auth_provider_request import UserAuthProviderRequest
from dupr_backend.models.wrapper import Wrapper

from dupr_backend.api_client import ApiClient
from dupr_backend.api_response import ApiResponse
from dupr_backend.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SocialMediaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def delete_provider_data_using_post(self, provider : Annotated[StrictStr, Field(..., description="provider")], version : Annotated[StrictStr, Field(..., description="version")], request : Annotated[StrictStr, Field(..., description="request")], **kwargs) -> DeleteUserResponse:  # noqa: E501
        """deleteProviderData  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_provider_data_using_post(provider, version, request, async_req=True)
        >>> result = thread.get()

        :param provider: provider (required)
        :type provider: str
        :param version: version (required)
        :type version: str
        :param request: request (required)
        :type request: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeleteUserResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_provider_data_using_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_provider_data_using_post_with_http_info(provider, version, request, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_provider_data_using_post_with_http_info(self, provider : Annotated[StrictStr, Field(..., description="provider")], version : Annotated[StrictStr, Field(..., description="version")], request : Annotated[StrictStr, Field(..., description="request")], **kwargs) -> ApiResponse:  # noqa: E501
        """deleteProviderData  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_provider_data_using_post_with_http_info(provider, version, request, async_req=True)
        >>> result = thread.get()

        :param provider: provider (required)
        :type provider: str
        :param version: version (required)
        :type version: str
        :param request: request (required)
        :type request: str
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
        :rtype: tuple(DeleteUserResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'provider',
            'version',
            'request'
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
                    " to method delete_provider_data_using_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['provider']:
            _path_params['provider'] = _params['provider']

        if _params['version']:
            _path_params['version'] = _params['version']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request'] is not None:
            _body_params = _params['request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "DeleteUserResponse",
            '403': None,
        }

        return self.api_client.call_api(
            '/social/{version}/{provider}/delete', 'POST',
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
    def get_instagram_login_using_get(self, code : Annotated[StrictStr, Field(..., description="code")], state : Annotated[StrictInt, Field(..., description="state")], version : Annotated[StrictStr, Field(..., description="version")], error : Annotated[Optional[StrictStr], Field(description="error")] = None, error_description : Annotated[Optional[StrictStr], Field(description="error_description")] = None, error_reason : Annotated[Optional[StrictStr], Field(description="error_reason")] = None, **kwargs) -> object:  # noqa: E501
        """getInstagramLogin  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instagram_login_using_get(code, state, version, error, error_description, error_reason, async_req=True)
        >>> result = thread.get()

        :param code: code (required)
        :type code: str
        :param state: state (required)
        :type state: int
        :param version: version (required)
        :type version: str
        :param error: error
        :type error: str
        :param error_description: error_description
        :type error_description: str
        :param error_reason: error_reason
        :type error_reason: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_instagram_login_using_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_instagram_login_using_get_with_http_info(code, state, version, error, error_description, error_reason, **kwargs)  # noqa: E501

    @validate_arguments
    def get_instagram_login_using_get_with_http_info(self, code : Annotated[StrictStr, Field(..., description="code")], state : Annotated[StrictInt, Field(..., description="state")], version : Annotated[StrictStr, Field(..., description="version")], error : Annotated[Optional[StrictStr], Field(description="error")] = None, error_description : Annotated[Optional[StrictStr], Field(description="error_description")] = None, error_reason : Annotated[Optional[StrictStr], Field(description="error_reason")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """getInstagramLogin  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instagram_login_using_get_with_http_info(code, state, version, error, error_description, error_reason, async_req=True)
        >>> result = thread.get()

        :param code: code (required)
        :type code: str
        :param state: state (required)
        :type state: int
        :param version: version (required)
        :type version: str
        :param error: error
        :type error: str
        :param error_description: error_description
        :type error_description: str
        :param error_reason: error_reason
        :type error_reason: str
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'code',
            'state',
            'version',
            'error',
            'error_description',
            'error_reason'
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
                    " to method get_instagram_login_using_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['version']:
            _path_params['version'] = _params['version']


        # process the query parameters
        _query_params = []
        if _params.get('code') is not None:  # noqa: E501
            _query_params.append(('code', _params['code']))

        if _params.get('error') is not None:  # noqa: E501
            _query_params.append(('error', _params['error']))

        if _params.get('error_description') is not None:  # noqa: E501
            _query_params.append(('error_description', _params['error_description']))

        if _params.get('error_reason') is not None:  # noqa: E501
            _query_params.append(('error_reason', _params['error_reason']))

        if _params.get('state') is not None:  # noqa: E501
            _query_params.append(('state', _params['state']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
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
            '200': "object",
            '403': None,
        }

        return self.api_client.call_api(
            '/social/{version}/instagram/login', 'GET',
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
    def get_login_detail_using_get(self, authorization : StrictStr, version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> Wrapper:  # noqa: E501
        """getLoginDetail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_login_detail_using_get(authorization, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
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
        :rtype: Wrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_login_detail_using_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_login_detail_using_get_with_http_info(authorization, version, **kwargs)  # noqa: E501

    @validate_arguments
    def get_login_detail_using_get_with_http_info(self, authorization : StrictStr, version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> ApiResponse:  # noqa: E501
        """getLoginDetail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_login_detail_using_get_with_http_info(authorization, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
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
        :rtype: tuple(Wrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
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
                    " to method get_login_detail_using_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
            '200': "Wrapper",
            '403': None,
        }

        return self.api_client.call_api(
            '/social/{version}/login', 'GET',
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
    def get_share_messages_using_get(self, authorization : StrictStr, version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> Wrapper:  # noqa: E501
        """getShareMessages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_share_messages_using_get(authorization, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
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
        :rtype: Wrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_share_messages_using_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_share_messages_using_get_with_http_info(authorization, version, **kwargs)  # noqa: E501

    @validate_arguments
    def get_share_messages_using_get_with_http_info(self, authorization : StrictStr, version : Annotated[StrictStr, Field(..., description="version")], **kwargs) -> ApiResponse:  # noqa: E501
        """getShareMessages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_share_messages_using_get_with_http_info(authorization, version, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
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
        :rtype: tuple(Wrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
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
                    " to method get_share_messages_using_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
            '200': "Wrapper",
            '403': None,
        }

        return self.api_client.call_api(
            '/social/share/{version}/message', 'GET',
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
    def update_social_login_details_using_put(self, authorization : StrictStr, version : Annotated[StrictStr, Field(..., description="version")], request : Annotated[UserAuthProviderRequest, Field(..., description="request")], **kwargs) -> Wrapper:  # noqa: E501
        """updateSocialLoginDetails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_social_login_details_using_put(authorization, version, request, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param version: version (required)
        :type version: str
        :param request: request (required)
        :type request: UserAuthProviderRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Wrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_social_login_details_using_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_social_login_details_using_put_with_http_info(authorization, version, request, **kwargs)  # noqa: E501

    @validate_arguments
    def update_social_login_details_using_put_with_http_info(self, authorization : StrictStr, version : Annotated[StrictStr, Field(..., description="version")], request : Annotated[UserAuthProviderRequest, Field(..., description="request")], **kwargs) -> ApiResponse:  # noqa: E501
        """updateSocialLoginDetails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_social_login_details_using_put_with_http_info(authorization, version, request, async_req=True)
        >>> result = thread.get()

        :param authorization: (required)
        :type authorization: str
        :param version: version (required)
        :type version: str
        :param request: request (required)
        :type request: UserAuthProviderRequest
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
        :rtype: tuple(Wrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
            'version',
            'request'
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
                    " to method update_social_login_details_using_put" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
        if _params['request'] is not None:
            _body_params = _params['request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Wrapper",
            '403': None,
        }

        return self.api_client.call_api(
            '/social/{version}/login', 'PUT',
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
