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


class LocalizationUpdate(object):
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
        'attributes': 'dict(str, object)',
        'frame': 'int',
        'height': 'float',
        'modified': 'bool',
        'parent': 'float',
        'u': 'float',
        'v': 'float',
        'width': 'float',
        'x': 'float',
        'y': 'float'
    }

    attribute_map = {
        'attributes': 'attributes',
        'frame': 'frame',
        'height': 'height',
        'modified': 'modified',
        'parent': 'parent',
        'u': 'u',
        'v': 'v',
        'width': 'width',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, attributes=None, frame=None, height=None, modified=None, parent=None, u=None, v=None, width=None, x=None, y=None, local_vars_configuration=None):  # noqa: E501
        """LocalizationUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._frame = None
        self._height = None
        self._modified = None
        self._parent = None
        self._u = None
        self._v = None
        self._width = None
        self._x = None
        self._y = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if frame is not None:
            self.frame = frame
        self.height = height
        self.modified = modified
        self.parent = parent
        self.u = u
        self.v = v
        self.width = width
        self.x = x
        self.y = y

    @property
    def attributes(self):
        """Gets the attributes of this LocalizationUpdate.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this LocalizationUpdate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LocalizationUpdate.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this LocalizationUpdate.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def frame(self):
        """Gets the frame of this LocalizationUpdate.  # noqa: E501

        Frame number of this localization if it is in a video.  # noqa: E501

        :return: The frame of this LocalizationUpdate.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this LocalizationUpdate.

        Frame number of this localization if it is in a video.  # noqa: E501

        :param frame: The frame of this LocalizationUpdate.  # noqa: E501
        :type: int
        """

        self._frame = frame

    @property
    def height(self):
        """Gets the height of this LocalizationUpdate.  # noqa: E501

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :return: The height of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this LocalizationUpdate.

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :param height: The height of this LocalizationUpdate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._height = height

    @property
    def modified(self):
        """Gets the modified of this LocalizationUpdate.  # noqa: E501

        Whether this localization was created in the web UI.  # noqa: E501

        :return: The modified of this LocalizationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this LocalizationUpdate.

        Whether this localization was created in the web UI.  # noqa: E501

        :param modified: The modified of this LocalizationUpdate.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def parent(self):
        """Gets the parent of this LocalizationUpdate.  # noqa: E501

        If a clone, the pk of the parent.  # noqa: E501

        :return: The parent of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this LocalizationUpdate.

        If a clone, the pk of the parent.  # noqa: E501

        :param parent: The parent of this LocalizationUpdate.  # noqa: E501
        :type: float
        """

        self._parent = parent

    @property
    def u(self):
        """Gets the u of this LocalizationUpdate.  # noqa: E501

        Horizontal vector component for `line` localization types.  # noqa: E501

        :return: The u of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._u

    @u.setter
    def u(self, u):
        """Sets the u of this LocalizationUpdate.

        Horizontal vector component for `line` localization types.  # noqa: E501

        :param u: The u of this LocalizationUpdate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                u is not None and u > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `u`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                u is not None and u < -1.0):  # noqa: E501
            raise ValueError("Invalid value for `u`, must be a value greater than or equal to `-1.0`")  # noqa: E501

        self._u = u

    @property
    def v(self):
        """Gets the v of this LocalizationUpdate.  # noqa: E501

        Vertical vector component for `line` localization types.  # noqa: E501

        :return: The v of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this LocalizationUpdate.

        Vertical vector component for `line` localization types.  # noqa: E501

        :param v: The v of this LocalizationUpdate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                v is not None and v > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `v`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                v is not None and v < -1.0):  # noqa: E501
            raise ValueError("Invalid value for `v`, must be a value greater than or equal to `-1.0`")  # noqa: E501

        self._v = v

    @property
    def width(self):
        """Gets the width of this LocalizationUpdate.  # noqa: E501

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :return: The width of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this LocalizationUpdate.

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :param width: The width of this LocalizationUpdate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._width = width

    @property
    def x(self):
        """Gets the x of this LocalizationUpdate.  # noqa: E501

        Normalized horizontal position of left edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :return: The x of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this LocalizationUpdate.

        Normalized horizontal position of left edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :param x: The x of this LocalizationUpdate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                x is not None and x > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `x`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x is not None and x < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `x`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this LocalizationUpdate.  # noqa: E501

        Normalized vertical position of top edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :return: The y of this LocalizationUpdate.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this LocalizationUpdate.

        Normalized vertical position of top edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :param y: The y of this LocalizationUpdate.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                y is not None and y > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `y`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y is not None and y < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `y`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._y = y

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
        if not isinstance(other, LocalizationUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalizationUpdate):
            return True

        return self.to_dict() != other.to_dict()
