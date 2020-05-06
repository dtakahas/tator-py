# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tator.configuration import Configuration


class LineProps(object):
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
        'x0': 'float',
        'x1': 'float',
        'y0': 'float',
        'y1': 'float'
    }

    attribute_map = {
        'x0': 'x0',
        'x1': 'x1',
        'y0': 'y0',
        'y1': 'y1'
    }

    def __init__(self, x0=None, x1=None, y0=None, y1=None, local_vars_configuration=None):  # noqa: E501
        """LineProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._x0 = None
        self._x1 = None
        self._y0 = None
        self._y1 = None
        self.discriminator = None

        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

    @property
    def x0(self):
        """Gets the x0 of this LineProps.  # noqa: E501

        Normalized horizontal position of start of line for `line` localization types.  # noqa: E501

        :return: The x0 of this LineProps.  # noqa: E501
        :rtype: float
        """
        return self._x0

    @x0.setter
    def x0(self, x0):
        """Sets the x0 of this LineProps.

        Normalized horizontal position of start of line for `line` localization types.  # noqa: E501

        :param x0: The x0 of this LineProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and x0 is None:  # noqa: E501
            raise ValueError("Invalid value for `x0`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x0 is not None and x0 > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `x0`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x0 is not None and x0 < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `x0`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._x0 = x0

    @property
    def x1(self):
        """Gets the x1 of this LineProps.  # noqa: E501

        Normalized horizontal position of end of line for `line` localization types.  # noqa: E501

        :return: The x1 of this LineProps.  # noqa: E501
        :rtype: float
        """
        return self._x1

    @x1.setter
    def x1(self, x1):
        """Sets the x1 of this LineProps.

        Normalized horizontal position of end of line for `line` localization types.  # noqa: E501

        :param x1: The x1 of this LineProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and x1 is None:  # noqa: E501
            raise ValueError("Invalid value for `x1`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x1 is not None and x1 > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `x1`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x1 is not None and x1 < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `x1`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._x1 = x1

    @property
    def y0(self):
        """Gets the y0 of this LineProps.  # noqa: E501

        Normalized vertical position of start of line for `line` localization types.  # noqa: E501

        :return: The y0 of this LineProps.  # noqa: E501
        :rtype: float
        """
        return self._y0

    @y0.setter
    def y0(self, y0):
        """Sets the y0 of this LineProps.

        Normalized vertical position of start of line for `line` localization types.  # noqa: E501

        :param y0: The y0 of this LineProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and y0 is None:  # noqa: E501
            raise ValueError("Invalid value for `y0`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y0 is not None and y0 > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `y0`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y0 is not None and y0 < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `y0`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._y0 = y0

    @property
    def y1(self):
        """Gets the y1 of this LineProps.  # noqa: E501

        Normalized vertical position of end of line for `line` localization types.  # noqa: E501

        :return: The y1 of this LineProps.  # noqa: E501
        :rtype: float
        """
        return self._y1

    @y1.setter
    def y1(self, y1):
        """Sets the y1 of this LineProps.

        Normalized vertical position of end of line for `line` localization types.  # noqa: E501

        :param y1: The y1 of this LineProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and y1 is None:  # noqa: E501
            raise ValueError("Invalid value for `y1`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y1 is not None and y1 > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `y1`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y1 is not None and y1 < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `y1`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._y1 = y1

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
        if not isinstance(other, LineProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineProps):
            return True

        return self.to_dict() != other.to_dict()
