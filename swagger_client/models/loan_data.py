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

class LoanData(object):
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
        'entity': 'str',
        'type': 'str',
        'balance': 'float',
        'description': 'str'
    }

    attribute_map = {
        'entity': 'entity',
        'type': 'type',
        'balance': 'balance',
        'description': 'description'
    }

    def __init__(self, entity=None, type=None, balance=None, description=None):  # noqa: E501
        """LoanData - a model defined in Swagger"""  # noqa: E501
        self._entity = None
        self._type = None
        self._balance = None
        self._description = None
        self.discriminator = None
        if entity is not None:
            self.entity = entity
        if type is not None:
            self.type = type
        if balance is not None:
            self.balance = balance
        if description is not None:
            self.description = description

    @property
    def entity(self):
        """Gets the entity of this LoanData.  # noqa: E501


        :return: The entity of this LoanData.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this LoanData.


        :param entity: The entity of this LoanData.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def type(self):
        """Gets the type of this LoanData.  # noqa: E501


        :return: The type of this LoanData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoanData.


        :param type: The type of this LoanData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def balance(self):
        """Gets the balance of this LoanData.  # noqa: E501


        :return: The balance of this LoanData.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this LoanData.


        :param balance: The balance of this LoanData.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def description(self):
        """Gets the description of this LoanData.  # noqa: E501


        :return: The description of this LoanData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoanData.


        :param description: The description of this LoanData.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(LoanData, dict):
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
        if not isinstance(other, LoanData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
