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


class ShippingAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, phone=None, address1=None, address2=None, city=None, region=None, country=None, zipcode=None, is_office_address=None, is_home_address=None):
        """
        ShippingAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'phone': 'str',
            'address1': 'str',
            'address2': 'str',
            'city': 'str',
            'region': 'str',
            'country': 'str',
            'zipcode': 'str',
            'is_office_address': 'bool',
            'is_home_address': 'bool'
        }

        self.attribute_map = {
            'name': '_name',
            'phone': '_phone',
            'address1': '_address1',
            'address2': '_address2',
            'city': '_city',
            'region': '_region',
            'country': '_country',
            'zipcode': '_zipcode',
            'is_office_address': '_isOfficeAddress',
            'is_home_address': '_isHomeAddress'
        }

        self._name = name
        self._phone = phone
        self._address1 = address1
        self._address2 = address2
        self._city = city
        self._region = region
        self._country = country
        self._zipcode = zipcode
        self._is_office_address = is_office_address
        self._is_home_address = is_home_address

    @property
    def name(self):
        """
        Gets the name of this ShippingAddress.
        Provide the full name associated with the address here. Concatenate first name and last name together if you collect them separately in your system.

        :return: The name of this ShippingAddress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ShippingAddress.
        Provide the full name associated with the address here. Concatenate first name and last name together if you collect them separately in your system.

        :param name: The name of this ShippingAddress.
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """
        Gets the phone of this ShippingAddress.
        The phone number associated with this address. Provide the phone number as a string starting with the country code. Use E.164 format or send in the standard national format of number's origin.

        :return: The phone of this ShippingAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this ShippingAddress.
        The phone number associated with this address. Provide the phone number as a string starting with the country code. Use E.164 format or send in the standard national format of number's origin.

        :param phone: The phone of this ShippingAddress.
        :type: str
        """

        self._phone = phone

    @property
    def address1(self):
        """
        Gets the address1 of this ShippingAddress.
        Address first line, e.g., \"C802 Nirvana Courtyard\".

        :return: The address1 of this ShippingAddress.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this ShippingAddress.
        Address first line, e.g., \"C802 Nirvana Courtyard\".

        :param address1: The address1 of this ShippingAddress.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this ShippingAddress.
        Address second line, e.g., \"Nirvana Country, Sector 50\".

        :return: The address2 of this ShippingAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this ShippingAddress.
        Address second line, e.g., \"Nirvana Country, Sector 50\".

        :param address2: The address2 of this ShippingAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this ShippingAddress.
        The city or town name, e.g., \"Gurgaon\" .

        :return: The city of this ShippingAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this ShippingAddress.
        The city or town name, e.g., \"Gurgaon\" .

        :param city: The city of this ShippingAddress.
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """
        Gets the region of this ShippingAddress.
        The region portion of the address. In the India, this corresponds to the state.

        :return: The region of this ShippingAddress.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ShippingAddress.
        The region portion of the address. In the India, this corresponds to the state.

        :param region: The region of this ShippingAddress.
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """
        Gets the country of this ShippingAddress.
        The [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code for the billing address, e.g., \"IN\" in case of India.

        :return: The country of this ShippingAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this ShippingAddress.
        The [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code for the billing address, e.g., \"IN\" in case of India.

        :param country: The country of this ShippingAddress.
        :type: str
        """

        self._country = country

    @property
    def zipcode(self):
        """
        Gets the zipcode of this ShippingAddress.
        The postal code associated with the address, e.g., \"122002\".

        :return: The zipcode of this ShippingAddress.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """
        Sets the zipcode of this ShippingAddress.
        The postal code associated with the address, e.g., \"122002\".

        :param zipcode: The zipcode of this ShippingAddress.
        :type: str
        """

        self._zipcode = zipcode

    @property
    def is_office_address(self):
        """
        Gets the is_office_address of this ShippingAddress.
        Is user chosen this address as office address.

        :return: The is_office_address of this ShippingAddress.
        :rtype: bool
        """
        return self._is_office_address

    @is_office_address.setter
    def is_office_address(self, is_office_address):
        """
        Sets the is_office_address of this ShippingAddress.
        Is user chosen this address as office address.

        :param is_office_address: The is_office_address of this ShippingAddress.
        :type: bool
        """

        self._is_office_address = is_office_address

    @property
    def is_home_address(self):
        """
        Gets the is_home_address of this ShippingAddress.
        Is user chosen this address as home address.

        :return: The is_home_address of this ShippingAddress.
        :rtype: bool
        """
        return self._is_home_address

    @is_home_address.setter
    def is_home_address(self, is_home_address):
        """
        Sets the is_home_address of this ShippingAddress.
        Is user chosen this address as home address.

        :param is_home_address: The is_home_address of this ShippingAddress.
        :type: bool
        """

        self._is_home_address = is_home_address

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
        if not isinstance(other, ShippingAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
