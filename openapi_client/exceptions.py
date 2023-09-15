# coding: utf-8

"""
    Геймтон DatsOrange

     ![image](./DatsOrange.png)  **Цель геймтона:** Остаться с самым большим количеством апельсинов в результате операций купли-продажи на бирже.     Командам предоставляется:   1. Биржа, на которой можно разместить заявки в определенное время.   2. Инструменты для торговли.    3. Стартовый баланс в апельсинах.   4. Новости, которые помогут строить прогнозы на рынке.   5. API.       # Биржа    Биржа работает (UTC+03:00):        - 15.09.2023 с 17:00 до 22:00;   - 16.09.2023 с 10:00 до 22:00.       Во время перерыва сервер не обрабатывает заказы игроков, все действия останавливаются.      На бирже есть компании с акциями, с течением времени добавляются новые компании. На стоимость компании, как и в реальном мире, влияют разные новостные события.     # Инструменты    Участники могут:      - выставлять лимитные заявки на покупку/продажу с указанием желаемой цены;   - продать/купить мгновенно по лучшей цене, которая сейчас есть в заявках на бирже.  Лимитные заявки действуют 1 минуту, и если не было желающих купить/продать по этой цене, через минуту они отклоняются.    # Стартовый баланс      Наша валюта - это Апельсины 🍊🍊🍊.    У каждого участника есть начальный баланс в апельсинах = 10000. Командам необходимо увеличить это количество. Стартовые апельсины при подсчете итогового результата учитываться не будут.       Например, в конце игры у вас на балансе 15000 апельсинов, значит ваш итог = 5000 (15000 - 10000).  # Новости На стоимость акций компании влияют происходящие в мире события. Новости содержат полезную информацию, а также список компаний, которые подвержены влиянию.     Пример новостей:   - -15% \"Лесной пожар уничтожил посевные, и урожай в этом году будет значительно меньше\".   - +20% \"Правительство приняло закон о криптовалюте, бизнес может проводить операции в крипте.\"    Где:    - “+/-” - позитивное или негативное влияние,    -  “15%” - прогнозный процент влияния новости на компании.    Процентные показатели являются прогнозными.     Новости также могут оповещать о других событиях. Следите за новостями.    # Кто победит    Победит активный участник рынка (не менее 100 заявок), у которого на момент закрытия биржи 16го числа останется самое большое положительное число апельсинов за вычетом стартового начисления от биржи.    За результатами команд можно следить на нашем новостном ресурсе по ссылке - https://datsteam.dev/datsorange/scene.      Текущий баланс на сайте - это приблизительное число, которое показывает сколько примерно апельсинов будет в случае продажи всех активов прямо сейчас. Однако в случае фактической продажи итог будет зависеть от спроса, поведения других игроков, поэтому не рекомендуем оставлять на самый последний момент выход в апельсины 🍊🍊🍊.            # API         Вы уже получили свой токен при регистрации, это означает, что в каждый запрос необходимо добавлять заголовок ‘token’ с отправленным вам значением.        # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import six


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None):
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
