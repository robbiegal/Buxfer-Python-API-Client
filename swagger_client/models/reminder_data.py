# coding: utf-8

"""
    Buxfer API

    Buxfer API based on their website.  -----------  Attention! --------------  THIS IS NOT AN OFFICIAL BUXFER.COM API  ----------- Attention! --------------  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: robbiegal@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReminderData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'start_date': 'str',
        'period': 'str',
        'amount': 'float',
        'account_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_date': 'startDate',
        'period': 'period',
        'amount': 'amount',
        'account_id': 'accountId'
    }

    def __init__(self, id=None, name=None, start_date=None, period=None, amount=None, account_id=None):  # noqa: E501
        """ReminderData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._start_date = None
        self._period = None
        self._amount = None
        self._account_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_date is not None:
            self.start_date = start_date
        if period is not None:
            self.period = period
        if amount is not None:
            self.amount = amount
        if account_id is not None:
            self.account_id = account_id

    @property
    def id(self):
        """Gets the id of this ReminderData.  # noqa: E501


        :return: The id of this ReminderData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReminderData.


        :param id: The id of this ReminderData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReminderData.  # noqa: E501


        :return: The name of this ReminderData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReminderData.


        :param name: The name of this ReminderData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this ReminderData.  # noqa: E501


        :return: The start_date of this ReminderData.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReminderData.


        :param start_date: The start_date of this ReminderData.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def period(self):
        """Gets the period of this ReminderData.  # noqa: E501


        :return: The period of this ReminderData.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ReminderData.


        :param period: The period of this ReminderData.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def amount(self):
        """Gets the amount of this ReminderData.  # noqa: E501


        :return: The amount of this ReminderData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ReminderData.


        :param amount: The amount of this ReminderData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def account_id(self):
        """Gets the account_id of this ReminderData.  # noqa: E501


        :return: The account_id of this ReminderData.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ReminderData.


        :param account_id: The account_id of this ReminderData.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ReminderData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReminderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
