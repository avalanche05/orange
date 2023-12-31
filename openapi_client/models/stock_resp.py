# coding: utf-8

"""
    Геймтон DatsOrange

     ![image](./DatsOrange.png)  **Цель геймтона:** Остаться с самым большим количеством апельсинов в результате операций купли-продажи на бирже.     Командам предоставляется:   1. Биржа, на которой можно разместить заявки в определенное время.   2. Инструменты для торговли.    3. Стартовый баланс в апельсинах.   4. Новости, которые помогут строить прогнозы на рынке.   5. API.       # Биржа    Биржа работает (UTC+03:00):        - 15.09.2023 с 17:00 до 22:00;   - 16.09.2023 с 10:00 до 22:00.       Во время перерыва сервер не обрабатывает заказы игроков, все действия останавливаются.      На бирже есть компании с акциями, с течением времени добавляются новые компании. На стоимость компании, как и в реальном мире, влияют разные новостные события.     # Инструменты    Участники могут:      - выставлять лимитные заявки на покупку/продажу с указанием желаемой цены;   - продать/купить мгновенно по лучшей цене, которая сейчас есть в заявках на бирже.  Лимитные заявки действуют 1 минуту, и если не было желающих купить/продать по этой цене, через минуту они отклоняются.    # Стартовый баланс      Наша валюта - это Апельсины 🍊🍊🍊.    У каждого участника есть начальный баланс в апельсинах = 10000. Командам необходимо увеличить это количество. Стартовые апельсины при подсчете итогового результата учитываться не будут.       Например, в конце игры у вас на балансе 15000 апельсинов, значит ваш итог = 5000 (15000 - 10000).  # Новости На стоимость акций компании влияют происходящие в мире события. Новости содержат полезную информацию, а также список компаний, которые подвержены влиянию.     Пример новостей:   - -15% \"Лесной пожар уничтожил посевные, и урожай в этом году будет значительно меньше\".   - +20% \"Правительство приняло закон о криптовалюте, бизнес может проводить операции в крипте.\"    Где:    - “+/-” - позитивное или негативное влияние,    -  “15%” - прогнозный процент влияния новости на компании.    Процентные показатели являются прогнозными.     Новости также могут оповещать о других событиях. Следите за новостями.    # Кто победит    Победит активный участник рынка (не менее 100 заявок), у которого на момент закрытия биржи 16го числа останется самое большое положительное число апельсинов за вычетом стартового начисления от биржи.    За результатами команд можно следить на нашем новостном ресурсе по ссылке - https://datsteam.dev/datsorange/scene.      Текущий баланс на сайте - это приблизительное число, которое показывает сколько примерно апельсинов будет в случае продажи всех активов прямо сейчас. Однако в случае фактической продажи итог будет зависеть от спроса, поведения других игроков, поэтому не рекомендуем оставлять на самый последний момент выход в апельсины 🍊🍊🍊.            # API         Вы уже получили свой токен при регистрации, это означает, что в каждый запрос необходимо добавлять заголовок ‘token’ с отправленным вам значением.        # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class StockResp(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'ticker': 'str',
        'bids': 'list[BidStat]'
    }

    attribute_map = {
        'id': 'id',
        'ticker': 'ticker',
        'bids': 'bids'
    }

    def __init__(self, id=None, ticker=None, bids=None, local_vars_configuration=None):  # noqa: E501
        """StockResp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._ticker = None
        self._bids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if bids is not None:
            self.bids = bids

    @property
    def id(self):
        """Gets the id of this StockResp.  # noqa: E501

        id  # noqa: E501

        :return: The id of this StockResp.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StockResp.

        id  # noqa: E501

        :param id: The id of this StockResp.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this StockResp.  # noqa: E501

        Тикер  # noqa: E501

        :return: The ticker of this StockResp.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockResp.

        Тикер  # noqa: E501

        :param ticker: The ticker of this StockResp.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def bids(self):
        """Gets the bids of this StockResp.  # noqa: E501

        Заявки  # noqa: E501

        :return: The bids of this StockResp.  # noqa: E501
        :rtype: list[BidStat]
        """
        return self._bids

    @bids.setter
    def bids(self, bids):
        """Sets the bids of this StockResp.

        Заявки  # noqa: E501

        :param bids: The bids of this StockResp.  # noqa: E501
        :type: list[BidStat]
        """

        self._bids = bids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StockResp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StockResp):
            return True

        return self.to_dict() != other.to_dict()
