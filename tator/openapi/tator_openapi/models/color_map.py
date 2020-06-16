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

from tator_openapi.configuration import Configuration


class ColorMap(object):
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
        'alpha_ranges': 'dict(str, list)',
        'default': 'object',
        'key': 'str',
        'map': 'dict(str, object)',
        'version': 'dict(str, object)'
    }

    attribute_map = {
        'alpha_ranges': 'alpha_ranges',
        'default': 'default',
        'key': 'key',
        'map': 'map',
        'version': 'version'
    }

    def __init__(self, alpha_ranges=None, default=None, key=None, map=None, version=None, local_vars_configuration=None):  # noqa: E501
        """ColorMap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alpha_ranges = None
        self._default = None
        self._key = None
        self._map = None
        self._version = None
        self.discriminator = None

        if alpha_ranges is not None:
            self.alpha_ranges = alpha_ranges
        if default is not None:
            self.default = default
        if key is not None:
            self.key = key
        if map is not None:
            self.map = map
        if version is not None:
            self.version = version

    @property
    def alpha_ranges(self):
        """Gets the alpha_ranges of this ColorMap.  # noqa: E501

        Map of attribute values to alpha level.  # noqa: E501

        :return: The alpha_ranges of this ColorMap.  # noqa: E501
        :rtype: dict(str, list)
        """
        return self._alpha_ranges

    @alpha_ranges.setter
    def alpha_ranges(self, alpha_ranges):
        """Sets the alpha_ranges of this ColorMap.

        Map of attribute values to alpha level.  # noqa: E501

        :param alpha_ranges: The alpha_ranges of this ColorMap.  # noqa: E501
        :type: dict(str, list)
        """

        self._alpha_ranges = alpha_ranges

    @property
    def default(self):
        """Gets the default of this ColorMap.  # noqa: E501

        RGB array, RGBA array, or hex string.  # noqa: E501

        :return: The default of this ColorMap.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ColorMap.

        RGB array, RGBA array, or hex string.  # noqa: E501

        :param default: The default of this ColorMap.  # noqa: E501
        :type: object
        """

        self._default = default

    @property
    def key(self):
        """Gets the key of this ColorMap.  # noqa: E501

        Attribute name.  # noqa: E501

        :return: The key of this ColorMap.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ColorMap.

        Attribute name.  # noqa: E501

        :param key: The key of this ColorMap.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def map(self):
        """Gets the map of this ColorMap.  # noqa: E501

        Map of attribute values to colors.  # noqa: E501

        :return: The map of this ColorMap.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this ColorMap.

        Map of attribute values to colors.  # noqa: E501

        :param map: The map of this ColorMap.  # noqa: E501
        :type: dict(str, object)
        """

        self._map = map

    @property
    def version(self):
        """Gets the version of this ColorMap.  # noqa: E501

        Map of version IDs to colors.  # noqa: E501

        :return: The version of this ColorMap.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ColorMap.

        Map of version IDs to colors.  # noqa: E501

        :param version: The version of this ColorMap.  # noqa: E501
        :type: dict(str, object)
        """

        self._version = version

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
        if not isinstance(other, ColorMap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ColorMap):
            return True

        return self.to_dict() != other.to_dict()
