# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs  # noqa: E501

    OpenAPI spec version: v1.0 alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dupr_backend.api_client import ApiClient


class ChatApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def chat_token_using_get(self, authorization, id, version, **kwargs):  # noqa: E501
        """chatToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_token_using_get(authorization, id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param int id: id (required)
        :param str version: version (required)
        :return: SingleWrapperOfChatTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_token_using_get_with_http_info(authorization, id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_token_using_get_with_http_info(authorization, id, version, **kwargs)  # noqa: E501
            return data

    def chat_token_using_get_with_http_info(self, authorization, id, version, **kwargs):  # noqa: E501
        """chatToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_token_using_get_with_http_info(authorization, id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param int id: id (required)
        :param str version: version (required)
        :return: SingleWrapperOfChatTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'id', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `chat_token_using_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `chat_token_using_get`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `chat_token_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/chat/{version}/token/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleWrapperOfChatTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_self_token_using_get(self, authorization, version, **kwargs):  # noqa: E501
        """getSelfToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_self_token_using_get(authorization, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param str version: version (required)
        :return: SingleWrapperOfChatTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_self_token_using_get_with_http_info(authorization, version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_self_token_using_get_with_http_info(authorization, version, **kwargs)  # noqa: E501
            return data

    def get_self_token_using_get_with_http_info(self, authorization, version, **kwargs):  # noqa: E501
        """getSelfToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_self_token_using_get_with_http_info(authorization, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param str version: version (required)
        :return: SingleWrapperOfChatTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_self_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_self_token_using_get`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_self_token_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/chat/{version}/token/self', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleWrapperOfChatTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user_using_post(self, body, authorization, version, **kwargs):  # noqa: E501
        """updateUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_using_post(body, authorization, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateUserRequest body: request (required)
        :param str authorization: (required)
        :param str version: version (required)
        :return: Wrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_using_post_with_http_info(body, authorization, version, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_using_post_with_http_info(body, authorization, version, **kwargs)  # noqa: E501
            return data

    def update_user_using_post_with_http_info(self, body, authorization, version, **kwargs):  # noqa: E501
        """updateUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_using_post_with_http_info(body, authorization, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateUserRequest body: request (required)
        :param str authorization: (required)
        :param str version: version (required)
        :return: Wrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_using_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `update_user_using_post`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `update_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/chat/{version}/update/user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wrapper',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
