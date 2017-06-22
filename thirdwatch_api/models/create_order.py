# coding: utf-8

"""
    Thirdwatch API

    The first version of the Thirdwatch API is an exciting step forward towards making it easier for developers to pass data to Thirdwatch.   # Introduction Once you've [registered your website/app](https://thirdwatch.ai) it's easy to start sending data to Thirdwatch.  All endpoints are only accessible via https and are located at `api.thirdwatch.ai`. For instance: you can send event at the moment by ```HTTP POST``` Request to the following URL with your API key in ```Header``` and ```JSON``` data in request body. ```   https://api.thirdwatch.ai/event/v1 ``` Every API request must contain ```API Key``` in header value ```X-THIRDWATCH-API-KEY```  Every event must contain your ```_userId``` (if this is not available, you can alternatively provide a ```_sessionId``` value also in ```_userId```).  # Score API The Score API is use to get an up to date cutomer trust score after you have sent transaction event and order successful. This API will provide the riskiness score of the order with reasons. Some examples of when you may want to check the score are before:    - Before Shippement of a package   - Finalizing a money transfer   - Giving access to a prearranged vacation rental   - Sending voucher on mail    ```   https://api.thirdwatch.ai/neo/v1/score?api_key=<your api key>&order_id=<Order id> ```  According to Score you can decide to take action Approve or Reject. Orders with score more than 70 will consider as Riskey orders. We'll provide some reasons also in rules section.  ## Response score API  ``` {   \"order_id\": \"OCT45671\",   \"user_id\": \"ajay_245\",   \"order_timestamp\": \"2017-05-09T09:40:45.717Z\",   \"score\": 82,   \"flag\": \"red\",     -\"reasons\": [     {         \"name\": \"_numOfFailedTransactions\",         \"display_name\": \"Number of failed transactions\",         \"flag\": \"green\",         \"value\": \"0\",         \"is_display\": true       },       {         \"name\": \"_accountAge\",         \"display_name\": \"Account age\",         \"flag\": \"red\",         \"value\": \"0\",         \"is_display\": true       },        {         \"name\": \"_numOfOrderSameIp\",         \"display_name\": \"Number of orders from same IP\",         \"flag\": \"red\",         \"value\": \"11\",         \"is_display\": true       }     ] } ``` 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateOrder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user_id=None, session_id=None, order_id=None, device_ip=None, origin_timestamp=None, user_email=None, amount=None, currency_code=None, has_expedited_shipping=None, shipping_method=None, order_referrer=None, is_pre_paid=None, is_gift=None, is_return=None, is_first_time_buyer=None, billing_address=None, shipping_address=None, payment_methods=None, promotions=None, items=None, custom_info=None):
        """
        CreateOrder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'str',
            'session_id': 'str',
            'order_id': 'str',
            'device_ip': 'str',
            'origin_timestamp': 'str',
            'user_email': 'str',
            'amount': 'str',
            'currency_code': 'str',
            'has_expedited_shipping': 'bool',
            'shipping_method': 'str',
            'order_referrer': 'str',
            'is_pre_paid': 'bool',
            'is_gift': 'bool',
            'is_return': 'bool',
            'is_first_time_buyer': 'bool',
            'billing_address': 'BillingAddress',
            'shipping_address': 'ShippingAddress',
            'payment_methods': 'list[PaymentMethod]',
            'promotions': 'list[Promotion]',
            'items': 'list[Item]',
            'custom_info': 'CustomInfo'
        }

        self.attribute_map = {
            'user_id': '_userId',
            'session_id': '_sessionId',
            'order_id': '_orderId',
            'device_ip': '_deviceIp',
            'origin_timestamp': '_originTimestamp',
            'user_email': '_userEmail',
            'amount': '_amount',
            'currency_code': '_currencyCode',
            'has_expedited_shipping': '_hasExpeditedShipping',
            'shipping_method': '_shippingMethod',
            'order_referrer': '_orderReferrer',
            'is_pre_paid': '_isPrePaid',
            'is_gift': '_isGift',
            'is_return': '_isReturn',
            'is_first_time_buyer': '_isFirstTimeBuyer',
            'billing_address': '_billingAddress',
            'shipping_address': '_shippingAddress',
            'payment_methods': '_paymentMethods',
            'promotions': '_promotions',
            'items': '_items',
            'custom_info': '_customInfo'
        }

        self._user_id = user_id
        self._session_id = session_id
        self._order_id = order_id
        self._device_ip = device_ip
        self._origin_timestamp = origin_timestamp
        self._user_email = user_email
        self._amount = amount
        self._currency_code = currency_code
        self._has_expedited_shipping = has_expedited_shipping
        self._shipping_method = shipping_method
        self._order_referrer = order_referrer
        self._is_pre_paid = is_pre_paid
        self._is_gift = is_gift
        self._is_return = is_return
        self._is_first_time_buyer = is_first_time_buyer
        self._billing_address = billing_address
        self._shipping_address = shipping_address
        self._payment_methods = payment_methods
        self._promotions = promotions
        self._items = items
        self._custom_info = custom_info

    @property
    def user_id(self):
        """
        Gets the user_id of this CreateOrder.
        The user's account ID according to your systems. Note that user IDs are case sensitive.

        :return: The user_id of this CreateOrder.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CreateOrder.
        The user's account ID according to your systems. Note that user IDs are case sensitive.

        :param user_id: The user_id of this CreateOrder.
        :type: str
        """

        self._user_id = user_id

    @property
    def session_id(self):
        """
        Gets the session_id of this CreateOrder.
        The user's current session ID, used to tie a user's action before and after login or account creation. Required if no user_id values is provided.

        :return: The session_id of this CreateOrder.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this CreateOrder.
        The user's current session ID, used to tie a user's action before and after login or account creation. Required if no user_id values is provided.

        :param session_id: The session_id of this CreateOrder.
        :type: str
        """

        self._session_id = session_id

    @property
    def order_id(self):
        """
        Gets the order_id of this CreateOrder.
        The ID for tracking this order in your system.

        :return: The order_id of this CreateOrder.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this CreateOrder.
        The ID for tracking this order in your system.

        :param order_id: The order_id of this CreateOrder.
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")

        self._order_id = order_id

    @property
    def device_ip(self):
        """
        Gets the device_ip of this CreateOrder.
        IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps.

        :return: The device_ip of this CreateOrder.
        :rtype: str
        """
        return self._device_ip

    @device_ip.setter
    def device_ip(self, device_ip):
        """
        Sets the device_ip of this CreateOrder.
        IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps.

        :param device_ip: The device_ip of this CreateOrder.
        :type: str
        """

        self._device_ip = device_ip

    @property
    def origin_timestamp(self):
        """
        Gets the origin_timestamp of this CreateOrder.
        Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string.

        :return: The origin_timestamp of this CreateOrder.
        :rtype: str
        """
        return self._origin_timestamp

    @origin_timestamp.setter
    def origin_timestamp(self, origin_timestamp):
        """
        Sets the origin_timestamp of this CreateOrder.
        Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string.

        :param origin_timestamp: The origin_timestamp of this CreateOrder.
        :type: str
        """

        self._origin_timestamp = origin_timestamp

    @property
    def user_email(self):
        """
        Gets the user_email of this CreateOrder.
        Email of the user creating this order. Note - If the user's email is also their account ID in your system, set both the userId and userEmail fields to their email address.

        :return: The user_email of this CreateOrder.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """
        Sets the user_email of this CreateOrder.
        Email of the user creating this order. Note - If the user's email is also their account ID in your system, set both the userId and userEmail fields to their email address.

        :param user_email: The user_email of this CreateOrder.
        :type: str
        """

        self._user_email = user_email

    @property
    def amount(self):
        """
        Gets the amount of this CreateOrder.
        The item unit price in numbers, in the base unit of the currency_code.e.g. \"2500\"

        :return: The amount of this CreateOrder.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this CreateOrder.
        The item unit price in numbers, in the base unit of the currency_code.e.g. \"2500\"

        :param amount: The amount of this CreateOrder.
        :type: str
        """

        self._amount = amount

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CreateOrder.
        The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems.

        :return: The currency_code of this CreateOrder.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CreateOrder.
        The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems.

        :param currency_code: The currency_code of this CreateOrder.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def has_expedited_shipping(self):
        """
        Gets the has_expedited_shipping of this CreateOrder.
        Whether the user requested priority/expedited shipping on their order.

        :return: The has_expedited_shipping of this CreateOrder.
        :rtype: bool
        """
        return self._has_expedited_shipping

    @has_expedited_shipping.setter
    def has_expedited_shipping(self, has_expedited_shipping):
        """
        Sets the has_expedited_shipping of this CreateOrder.
        Whether the user requested priority/expedited shipping on their order.

        :param has_expedited_shipping: The has_expedited_shipping of this CreateOrder.
        :type: bool
        """

        self._has_expedited_shipping = has_expedited_shipping

    @property
    def shipping_method(self):
        """
        Gets the shipping_method of this CreateOrder.
        Indicates the method of delivery to the user. e.g. _electronic, _physical

        :return: The shipping_method of this CreateOrder.
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """
        Sets the shipping_method of this CreateOrder.
        Indicates the method of delivery to the user. e.g. _electronic, _physical

        :param shipping_method: The shipping_method of this CreateOrder.
        :type: str
        """

        self._shipping_method = shipping_method

    @property
    def order_referrer(self):
        """
        Gets the order_referrer of this CreateOrder.
        Referer website or user name.

        :return: The order_referrer of this CreateOrder.
        :rtype: str
        """
        return self._order_referrer

    @order_referrer.setter
    def order_referrer(self, order_referrer):
        """
        Sets the order_referrer of this CreateOrder.
        Referer website or user name.

        :param order_referrer: The order_referrer of this CreateOrder.
        :type: str
        """

        self._order_referrer = order_referrer

    @property
    def is_pre_paid(self):
        """
        Gets the is_pre_paid of this CreateOrder.
        is order is prepaid.

        :return: The is_pre_paid of this CreateOrder.
        :rtype: bool
        """
        return self._is_pre_paid

    @is_pre_paid.setter
    def is_pre_paid(self, is_pre_paid):
        """
        Sets the is_pre_paid of this CreateOrder.
        is order is prepaid.

        :param is_pre_paid: The is_pre_paid of this CreateOrder.
        :type: bool
        """

        self._is_pre_paid = is_pre_paid

    @property
    def is_gift(self):
        """
        Gets the is_gift of this CreateOrder.
        Is user chosen gift pack.

        :return: The is_gift of this CreateOrder.
        :rtype: bool
        """
        return self._is_gift

    @is_gift.setter
    def is_gift(self, is_gift):
        """
        Sets the is_gift of this CreateOrder.
        Is user chosen gift pack.

        :param is_gift: The is_gift of this CreateOrder.
        :type: bool
        """

        self._is_gift = is_gift

    @property
    def is_return(self):
        """
        Gets the is_return of this CreateOrder.
        Is this return order.

        :return: The is_return of this CreateOrder.
        :rtype: bool
        """
        return self._is_return

    @is_return.setter
    def is_return(self, is_return):
        """
        Sets the is_return of this CreateOrder.
        Is this return order.

        :param is_return: The is_return of this CreateOrder.
        :type: bool
        """

        self._is_return = is_return

    @property
    def is_first_time_buyer(self):
        """
        Gets the is_first_time_buyer of this CreateOrder.
        Is user first time buyer.

        :return: The is_first_time_buyer of this CreateOrder.
        :rtype: bool
        """
        return self._is_first_time_buyer

    @is_first_time_buyer.setter
    def is_first_time_buyer(self, is_first_time_buyer):
        """
        Sets the is_first_time_buyer of this CreateOrder.
        Is user first time buyer.

        :param is_first_time_buyer: The is_first_time_buyer of this CreateOrder.
        :type: bool
        """

        self._is_first_time_buyer = is_first_time_buyer

    @property
    def billing_address(self):
        """
        Gets the billing_address of this CreateOrder.

        :return: The billing_address of this CreateOrder.
        :rtype: BillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this CreateOrder.

        :param billing_address: The billing_address of this CreateOrder.
        :type: BillingAddress
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this CreateOrder.

        :return: The shipping_address of this CreateOrder.
        :rtype: ShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this CreateOrder.

        :param shipping_address: The shipping_address of this CreateOrder.
        :type: ShippingAddress
        """

        self._shipping_address = shipping_address

    @property
    def payment_methods(self):
        """
        Gets the payment_methods of this CreateOrder.
        The payment information associated with this order. Represented as an array of nested payment_method objects containing payment type, payment gateway, credit card bin, etc.

        :return: The payment_methods of this CreateOrder.
        :rtype: list[PaymentMethod]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """
        Sets the payment_methods of this CreateOrder.
        The payment information associated with this order. Represented as an array of nested payment_method objects containing payment type, payment gateway, credit card bin, etc.

        :param payment_methods: The payment_methods of this CreateOrder.
        :type: list[PaymentMethod]
        """

        self._payment_methods = payment_methods

    @property
    def promotions(self):
        """
        Gets the promotions of this CreateOrder.
        The list of promotions that apply to this order. You can add one or more promotions when creating or updating an order. Represented as a JSON array of promotion objects. You can also separately add promotions to the account via the addPromotion event.

        :return: The promotions of this CreateOrder.
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """
        Sets the promotions of this CreateOrder.
        The list of promotions that apply to this order. You can add one or more promotions when creating or updating an order. Represented as a JSON array of promotion objects. You can also separately add promotions to the account via the addPromotion event.

        :param promotions: The promotions of this CreateOrder.
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def items(self):
        """
        Gets the items of this CreateOrder.
        The list of items ordered. Represented as a JSON array of item

        :return: The items of this CreateOrder.
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CreateOrder.
        The list of items ordered. Represented as a JSON array of item

        :param items: The items of this CreateOrder.
        :type: list[Item]
        """

        self._items = items

    @property
    def custom_info(self):
        """
        Gets the custom_info of this CreateOrder.

        :return: The custom_info of this CreateOrder.
        :rtype: CustomInfo
        """
        return self._custom_info

    @custom_info.setter
    def custom_info(self, custom_info):
        """
        Sets the custom_info of this CreateOrder.

        :param custom_info: The custom_info of this CreateOrder.
        :type: CustomInfo
        """

        self._custom_info = custom_info

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CreateOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other