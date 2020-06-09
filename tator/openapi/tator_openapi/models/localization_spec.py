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


class LocalizationSpec(object):
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
        'frame': 'int',
        'height': 'float',
        'media_id': 'int',
        'modified': 'bool',
        'parent': 'float',
        'type': 'int',
        'u': 'float',
        'v': 'float',
        'version': 'int',
        'width': 'float',
        'x': 'float',
        'y': 'float'
    }

    attribute_map = {
        'frame': 'frame',
        'height': 'height',
        'media_id': 'media_id',
        'modified': 'modified',
        'parent': 'parent',
        'type': 'type',
        'u': 'u',
        'v': 'v',
        'version': 'version',
        'width': 'width',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, frame=0, height=None, media_id=None, modified=None, parent=None, type=None, u=None, v=None, version=None, width=None, x=None, y=None, local_vars_configuration=None):  # noqa: E501
        """LocalizationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._frame = None
        self._height = None
        self._media_id = None
        self._modified = None
        self._parent = None
        self._type = None
        self._u = None
        self._v = None
        self._version = None
        self._width = None
        self._x = None
        self._y = None
        self.discriminator = None

        self.frame = frame
        self.height = height
        self.media_id = media_id
        self.modified = modified
        self.parent = parent
        self.type = type
        self.u = u
        self.v = v
        if version is not None:
            self.version = version
        self.width = width
        self.x = x
        self.y = y

    @property
    def frame(self):
        """Gets the frame of this LocalizationSpec.  # noqa: E501

        Frame number of this localization if it is in a video.  # noqa: E501

        :return: The frame of this LocalizationSpec.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this LocalizationSpec.

        Frame number of this localization if it is in a video.  # noqa: E501

        :param frame: The frame of this LocalizationSpec.  # noqa: E501
        :type frame: int
        """
        if self.local_vars_configuration.client_side_validation and frame is None:  # noqa: E501
            raise ValueError("Invalid value for `frame`, must not be `None`")  # noqa: E501

        self._frame = frame

    @property
    def height(self):
        """Gets the height of this LocalizationSpec.  # noqa: E501

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :return: The height of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this LocalizationSpec.

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :param height: The height of this LocalizationSpec.  # noqa: E501
        :type height: float
        """
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._height = height

    @property
    def media_id(self):
        """Gets the media_id of this LocalizationSpec.  # noqa: E501

        Unique integer identifying a media.  # noqa: E501

        :return: The media_id of this LocalizationSpec.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this LocalizationSpec.

        Unique integer identifying a media.  # noqa: E501

        :param media_id: The media_id of this LocalizationSpec.  # noqa: E501
        :type media_id: int
        """
        if self.local_vars_configuration.client_side_validation and media_id is None:  # noqa: E501
            raise ValueError("Invalid value for `media_id`, must not be `None`")  # noqa: E501

        self._media_id = media_id

    @property
    def modified(self):
        """Gets the modified of this LocalizationSpec.  # noqa: E501

        Whether this localization was created in the web UI.  # noqa: E501

        :return: The modified of this LocalizationSpec.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this LocalizationSpec.

        Whether this localization was created in the web UI.  # noqa: E501

        :param modified: The modified of this LocalizationSpec.  # noqa: E501
        :type modified: bool
        """

        self._modified = modified

    @property
    def parent(self):
        """Gets the parent of this LocalizationSpec.  # noqa: E501

        If a clone, the pk of the parent.  # noqa: E501

        :return: The parent of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this LocalizationSpec.

        If a clone, the pk of the parent.  # noqa: E501

        :param parent: The parent of this LocalizationSpec.  # noqa: E501
        :type parent: float
        """

        self._parent = parent

    @property
    def type(self):
        """Gets the type of this LocalizationSpec.  # noqa: E501

        Unique integer identifying a localization type.  # noqa: E501

        :return: The type of this LocalizationSpec.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LocalizationSpec.

        Unique integer identifying a localization type.  # noqa: E501

        :param type: The type of this LocalizationSpec.  # noqa: E501
        :type type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def u(self):
        """Gets the u of this LocalizationSpec.  # noqa: E501

        Horizontal vector component for `line` localization types.  # noqa: E501

        :return: The u of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._u

    @u.setter
    def u(self, u):
        """Sets the u of this LocalizationSpec.

        Horizontal vector component for `line` localization types.  # noqa: E501

        :param u: The u of this LocalizationSpec.  # noqa: E501
        :type u: float
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
        """Gets the v of this LocalizationSpec.  # noqa: E501

        Vertical vector component for `line` localization types.  # noqa: E501

        :return: The v of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this LocalizationSpec.

        Vertical vector component for `line` localization types.  # noqa: E501

        :param v: The v of this LocalizationSpec.  # noqa: E501
        :type v: float
        """
        if (self.local_vars_configuration.client_side_validation and
                v is not None and v > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `v`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                v is not None and v < -1.0):  # noqa: E501
            raise ValueError("Invalid value for `v`, must be a value greater than or equal to `-1.0`")  # noqa: E501

        self._v = v

    @property
    def version(self):
        """Gets the version of this LocalizationSpec.  # noqa: E501

        Unique integer identifying the version.  # noqa: E501

        :return: The version of this LocalizationSpec.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LocalizationSpec.

        Unique integer identifying the version.  # noqa: E501

        :param version: The version of this LocalizationSpec.  # noqa: E501
        :type version: int
        """

        self._version = version

    @property
    def width(self):
        """Gets the width of this LocalizationSpec.  # noqa: E501

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :return: The width of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this LocalizationSpec.

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :param width: The width of this LocalizationSpec.  # noqa: E501
        :type width: float
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
        """Gets the x of this LocalizationSpec.  # noqa: E501

        Normalized horizontal position of left edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :return: The x of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this LocalizationSpec.

        Normalized horizontal position of left edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :param x: The x of this LocalizationSpec.  # noqa: E501
        :type x: float
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
        """Gets the y of this LocalizationSpec.  # noqa: E501

        Normalized vertical position of top edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :return: The y of this LocalizationSpec.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this LocalizationSpec.

        Normalized vertical position of top edge of bounding box for `box` localization types, start of line for `line` localization types, or position of dot for `dot` localization types.  # noqa: E501

        :param y: The y of this LocalizationSpec.  # noqa: E501
        :type y: float
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
        if not isinstance(other, LocalizationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalizationSpec):
            return True

        return self.to_dict() != other.to_dict()