# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.9
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LinearSetMarginResult(object):
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
        'position_list_result': 'object',
        'available_balance': 'float',
        'wallet_balance': 'float'
    }

    attribute_map = {
        'position_list_result': 'PositionListResult',
        'available_balance': 'available_balance',
        'wallet_balance': 'wallet_balance'
    }

    def __init__(self, position_list_result=None, available_balance=None, wallet_balance=None):  # noqa: E501
        """LinearSetMarginResult - a model defined in Swagger"""  # noqa: E501

        self._position_list_result = None
        self._available_balance = None
        self._wallet_balance = None
        self.discriminator = None

        if position_list_result is not None:
            self.position_list_result = position_list_result
        if available_balance is not None:
            self.available_balance = available_balance
        if wallet_balance is not None:
            self.wallet_balance = wallet_balance

    @property
    def position_list_result(self):
        """Gets the position_list_result of this LinearSetMarginResult.  # noqa: E501


        :return: The position_list_result of this LinearSetMarginResult.  # noqa: E501
        :rtype: object
        """
        return self._position_list_result

    @position_list_result.setter
    def position_list_result(self, position_list_result):
        """Sets the position_list_result of this LinearSetMarginResult.


        :param position_list_result: The position_list_result of this LinearSetMarginResult.  # noqa: E501
        :type: object
        """

        self._position_list_result = position_list_result

    @property
    def available_balance(self):
        """Gets the available_balance of this LinearSetMarginResult.  # noqa: E501


        :return: The available_balance of this LinearSetMarginResult.  # noqa: E501
        :rtype: float
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this LinearSetMarginResult.


        :param available_balance: The available_balance of this LinearSetMarginResult.  # noqa: E501
        :type: float
        """

        self._available_balance = available_balance

    @property
    def wallet_balance(self):
        """Gets the wallet_balance of this LinearSetMarginResult.  # noqa: E501


        :return: The wallet_balance of this LinearSetMarginResult.  # noqa: E501
        :rtype: float
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """Sets the wallet_balance of this LinearSetMarginResult.


        :param wallet_balance: The wallet_balance of this LinearSetMarginResult.  # noqa: E501
        :type: float
        """

        self._wallet_balance = wallet_balance

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
        if issubclass(LinearSetMarginResult, dict):
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
        if not isinstance(other, LinearSetMarginResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
