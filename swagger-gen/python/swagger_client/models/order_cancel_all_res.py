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


class OrderCancelAllRes(object):
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
        'cl_ord_id': 'str',
        'user_id': 'float',
        'side': 'str',
        'order_type': 'str',
        'price': 'str',
        'qty': 'str',
        'time_in_force': 'str',
        'create_type': 'str',
        'order_status': 'str',
        'leaves_qty': 'float',
        'leaves_value': 'float',
        'created_at': 'str',
        'updated_at': 'str',
        'cross_status': 'str',
        'cross_seq': 'float'
    }

    attribute_map = {
        'cl_ord_id': 'clOrdID',
        'user_id': 'user_id',
        'side': 'side',
        'order_type': 'order_type',
        'price': 'price',
        'qty': 'qty',
        'time_in_force': 'time_in_force',
        'create_type': 'create_type',
        'order_status': 'order_status',
        'leaves_qty': 'leaves_qty',
        'leaves_value': 'leaves_value',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cross_status': 'cross_status',
        'cross_seq': 'cross_seq'
    }

    def __init__(self, cl_ord_id=None, user_id=None, side=None, order_type=None, price=None, qty=None, time_in_force=None, create_type=None, order_status=None, leaves_qty=None, leaves_value=None, created_at=None, updated_at=None, cross_status=None, cross_seq=None):  # noqa: E501
        """OrderCancelAllRes - a model defined in Swagger"""  # noqa: E501

        self._cl_ord_id = None
        self._user_id = None
        self._side = None
        self._order_type = None
        self._price = None
        self._qty = None
        self._time_in_force = None
        self._create_type = None
        self._order_status = None
        self._leaves_qty = None
        self._leaves_value = None
        self._created_at = None
        self._updated_at = None
        self._cross_status = None
        self._cross_seq = None
        self.discriminator = None

        if cl_ord_id is not None:
            self.cl_ord_id = cl_ord_id
        if user_id is not None:
            self.user_id = user_id
        if side is not None:
            self.side = side
        if order_type is not None:
            self.order_type = order_type
        if price is not None:
            self.price = price
        if qty is not None:
            self.qty = qty
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if create_type is not None:
            self.create_type = create_type
        if order_status is not None:
            self.order_status = order_status
        if leaves_qty is not None:
            self.leaves_qty = leaves_qty
        if leaves_value is not None:
            self.leaves_value = leaves_value
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if cross_status is not None:
            self.cross_status = cross_status
        if cross_seq is not None:
            self.cross_seq = cross_seq

    @property
    def cl_ord_id(self):
        """Gets the cl_ord_id of this OrderCancelAllRes.  # noqa: E501


        :return: The cl_ord_id of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._cl_ord_id

    @cl_ord_id.setter
    def cl_ord_id(self, cl_ord_id):
        """Sets the cl_ord_id of this OrderCancelAllRes.


        :param cl_ord_id: The cl_ord_id of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._cl_ord_id = cl_ord_id

    @property
    def user_id(self):
        """Gets the user_id of this OrderCancelAllRes.  # noqa: E501


        :return: The user_id of this OrderCancelAllRes.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OrderCancelAllRes.


        :param user_id: The user_id of this OrderCancelAllRes.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def side(self):
        """Gets the side of this OrderCancelAllRes.  # noqa: E501


        :return: The side of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OrderCancelAllRes.


        :param side: The side of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def order_type(self):
        """Gets the order_type of this OrderCancelAllRes.  # noqa: E501


        :return: The order_type of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this OrderCancelAllRes.


        :param order_type: The order_type of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def price(self):
        """Gets the price of this OrderCancelAllRes.  # noqa: E501


        :return: The price of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderCancelAllRes.


        :param price: The price of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this OrderCancelAllRes.  # noqa: E501


        :return: The qty of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this OrderCancelAllRes.


        :param qty: The qty of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._qty = qty

    @property
    def time_in_force(self):
        """Gets the time_in_force of this OrderCancelAllRes.  # noqa: E501


        :return: The time_in_force of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this OrderCancelAllRes.


        :param time_in_force: The time_in_force of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._time_in_force = time_in_force

    @property
    def create_type(self):
        """Gets the create_type of this OrderCancelAllRes.  # noqa: E501


        :return: The create_type of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        """Sets the create_type of this OrderCancelAllRes.


        :param create_type: The create_type of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._create_type = create_type

    @property
    def order_status(self):
        """Gets the order_status of this OrderCancelAllRes.  # noqa: E501


        :return: The order_status of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this OrderCancelAllRes.


        :param order_status: The order_status of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._order_status = order_status

    @property
    def leaves_qty(self):
        """Gets the leaves_qty of this OrderCancelAllRes.  # noqa: E501


        :return: The leaves_qty of this OrderCancelAllRes.  # noqa: E501
        :rtype: float
        """
        return self._leaves_qty

    @leaves_qty.setter
    def leaves_qty(self, leaves_qty):
        """Sets the leaves_qty of this OrderCancelAllRes.


        :param leaves_qty: The leaves_qty of this OrderCancelAllRes.  # noqa: E501
        :type: float
        """

        self._leaves_qty = leaves_qty

    @property
    def leaves_value(self):
        """Gets the leaves_value of this OrderCancelAllRes.  # noqa: E501


        :return: The leaves_value of this OrderCancelAllRes.  # noqa: E501
        :rtype: float
        """
        return self._leaves_value

    @leaves_value.setter
    def leaves_value(self, leaves_value):
        """Sets the leaves_value of this OrderCancelAllRes.


        :param leaves_value: The leaves_value of this OrderCancelAllRes.  # noqa: E501
        :type: float
        """

        self._leaves_value = leaves_value

    @property
    def created_at(self):
        """Gets the created_at of this OrderCancelAllRes.  # noqa: E501


        :return: The created_at of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrderCancelAllRes.


        :param created_at: The created_at of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OrderCancelAllRes.  # noqa: E501


        :return: The updated_at of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OrderCancelAllRes.


        :param updated_at: The updated_at of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def cross_status(self):
        """Gets the cross_status of this OrderCancelAllRes.  # noqa: E501


        :return: The cross_status of this OrderCancelAllRes.  # noqa: E501
        :rtype: str
        """
        return self._cross_status

    @cross_status.setter
    def cross_status(self, cross_status):
        """Sets the cross_status of this OrderCancelAllRes.


        :param cross_status: The cross_status of this OrderCancelAllRes.  # noqa: E501
        :type: str
        """

        self._cross_status = cross_status

    @property
    def cross_seq(self):
        """Gets the cross_seq of this OrderCancelAllRes.  # noqa: E501


        :return: The cross_seq of this OrderCancelAllRes.  # noqa: E501
        :rtype: float
        """
        return self._cross_seq

    @cross_seq.setter
    def cross_seq(self, cross_seq):
        """Sets the cross_seq of this OrderCancelAllRes.


        :param cross_seq: The cross_seq of this OrderCancelAllRes.  # noqa: E501
        :type: float
        """

        self._cross_seq = cross_seq

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
        if issubclass(OrderCancelAllRes, dict):
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
        if not isinstance(other, OrderCancelAllRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
