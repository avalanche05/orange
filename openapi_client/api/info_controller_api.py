# coding: utf-8

"""
    Геймтон DatsOrange

     ![image](./DatsOrange.png)  **Цель геймтона:** Остаться с самым большим количеством апельсинов в результате операций купли-продажи на бирже.     Командам предоставляется:   1. Биржа, на которой можно разместить заявки в определенное время.   2. Инструменты для торговли.    3. Стартовый баланс в апельсинах.   4. Новости, которые помогут строить прогнозы на рынке.   5. API.       # Биржа    Биржа работает (UTC+03:00):        - 15.09.2023 с 17:00 до 22:00;   - 16.09.2023 с 10:00 до 22:00.       Во время перерыва сервер не обрабатывает заказы игроков, все действия останавливаются.      На бирже есть компании с акциями, с течением времени добавляются новые компании. На стоимость компании, как и в реальном мире, влияют разные новостные события.     # Инструменты    Участники могут:      - выставлять лимитные заявки на покупку/продажу с указанием желаемой цены;   - продать/купить мгновенно по лучшей цене, которая сейчас есть в заявках на бирже.  Лимитные заявки действуют 1 минуту, и если не было желающих купить/продать по этой цене, через минуту они отклоняются.    # Стартовый баланс      Наша валюта - это Апельсины 🍊🍊🍊.    У каждого участника есть начальный баланс в апельсинах = 10000. Командам необходимо увеличить это количество. Стартовые апельсины при подсчете итогового результата учитываться не будут.       Например, в конце игры у вас на балансе 15000 апельсинов, значит ваш итог = 5000 (15000 - 10000).  # Новости На стоимость акций компании влияют происходящие в мире события. Новости содержат полезную информацию, а также список компаний, которые подвержены влиянию.     Пример новостей:   - -15% \"Лесной пожар уничтожил посевные, и урожай в этом году будет значительно меньше\".   - +20% \"Правительство приняло закон о криптовалюте, бизнес может проводить операции в крипте.\"    Где:    - “+/-” - позитивное или негативное влияние,    -  “15%” - прогнозный процент влияния новости на компании.    Процентные показатели являются прогнозными.     Новости также могут оповещать о других событиях. Следите за новостями.    # Кто победит    Победит активный участник рынка (не менее 100 заявок), у которого на момент закрытия биржи 16го числа останется самое большое положительное число апельсинов за вычетом стартового начисления от биржи.    За результатами команд можно следить на нашем новостном ресурсе по ссылке - https://datsteam.dev/datsorange/scene.      Текущий баланс на сайте - это приблизительное число, которое показывает сколько примерно апельсинов будет в случае продажи всех активов прямо сейчас. Однако в случае фактической продажи итог будет зависеть от спроса, поведения других игроков, поэтому не рекомендуем оставлять на самый последний момент выход в апельсины 🍊🍊🍊.            # API         Вы уже получили свой токен при регистрации, это означает, что в каждый запрос необходимо добавлять заголовок ‘token’ с отправленным вам значением.        # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class InfoControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_info(self, token, **kwargs):  # noqa: E501
        """Информация о счете  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.account_info_with_http_info(token, **kwargs)  # noqa: E501

    def account_info_with_http_info(self, token, **kwargs):  # noqa: E501
        """Информация о счете  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_info_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InfoResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `account_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'token' in local_var_params:
            header_params['token'] = local_var_params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
