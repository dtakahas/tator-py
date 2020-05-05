# coding: utf-8

"""
    Tator REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Box(object):
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
        'id': 'int',
        'project': 'int',
        'meta': 'int',
        'media': 'int',
        'thumbnail_image': 'str',
        'modified': 'bool',
        'version': 'int',
        'email': 'str',
        'frame': 'int',
        'attributes': 'dict(str, object)',
        'x': 'float',
        'y': 'float',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'id': 'id',
        'project': 'project',
        'meta': 'meta',
        'media': 'media',
        'thumbnail_image': 'thumbnail_image',
        'modified': 'modified',
        'version': 'version',
        'email': 'email',
        'frame': 'frame',
        'attributes': 'attributes',
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, id=None, project=None, meta=None, media=None, thumbnail_image=None, modified=None, version=None, email=None, frame=None, attributes=None, x=None, y=None, width=None, height=None):  # noqa: E501
        """Box - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project = None
        self._meta = None
        self._media = None
        self._thumbnail_image = None
        self._modified = None
        self._version = None
        self._email = None
        self._frame = None
        self._attributes = None
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if meta is not None:
            self.meta = meta
        if media is not None:
            self.media = media
        if thumbnail_image is not None:
            self.thumbnail_image = thumbnail_image
        if modified is not None:
            self.modified = modified
        if version is not None:
            self.version = version
        if email is not None:
            self.email = email
        if frame is not None:
            self.frame = frame
        if attributes is not None:
            self.attributes = attributes
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def id(self):
        """Gets the id of this Box.  # noqa: E501

        Unique integer identifying this localization.  # noqa: E501

        :return: The id of this Box.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Box.

        Unique integer identifying this localization.  # noqa: E501

        :param id: The id of this Box.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this Box.  # noqa: E501

        Unique integer identifying project of this localization.  # noqa: E501

        :return: The project of this Box.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Box.

        Unique integer identifying project of this localization.  # noqa: E501

        :param project: The project of this Box.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def meta(self):
        """Gets the meta of this Box.  # noqa: E501

        Unique integer identifying entity type of this localization.  # noqa: E501

        :return: The meta of this Box.  # noqa: E501
        :rtype: int
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Box.

        Unique integer identifying entity type of this localization.  # noqa: E501

        :param meta: The meta of this Box.  # noqa: E501
        :type: int
        """

        self._meta = meta

    @property
    def media(self):
        """Gets the media of this Box.  # noqa: E501

        Unique integer identifying media of this localization.  # noqa: E501

        :return: The media of this Box.  # noqa: E501
        :rtype: int
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this Box.

        Unique integer identifying media of this localization.  # noqa: E501

        :param media: The media of this Box.  # noqa: E501
        :type: int
        """

        self._media = media

    @property
    def thumbnail_image(self):
        """Gets the thumbnail_image of this Box.  # noqa: E501

        URL of thumbnail corresponding to this localization.  # noqa: E501

        :return: The thumbnail_image of this Box.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_image

    @thumbnail_image.setter
    def thumbnail_image(self, thumbnail_image):
        """Sets the thumbnail_image of this Box.

        URL of thumbnail corresponding to this localization.  # noqa: E501

        :param thumbnail_image: The thumbnail_image of this Box.  # noqa: E501
        :type: str
        """

        self._thumbnail_image = thumbnail_image

    @property
    def modified(self):
        """Gets the modified of this Box.  # noqa: E501

        Indicates whether this localization has been modified in the web UI.  # noqa: E501

        :return: The modified of this Box.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Box.

        Indicates whether this localization has been modified in the web UI.  # noqa: E501

        :param modified: The modified of this Box.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def version(self):
        """Gets the version of this Box.  # noqa: E501

        Unique integer identifying a version.  # noqa: E501

        :return: The version of this Box.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Box.

        Unique integer identifying a version.  # noqa: E501

        :param version: The version of this Box.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def email(self):
        """Gets the email of this Box.  # noqa: E501

        Email of last user who modified/created this localization.  # noqa: E501

        :return: The email of this Box.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Box.

        Email of last user who modified/created this localization.  # noqa: E501

        :param email: The email of this Box.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def frame(self):
        """Gets the frame of this Box.  # noqa: E501

        Frame number of this localization if it is in a video.  # noqa: E501

        :return: The frame of this Box.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this Box.

        Frame number of this localization if it is in a video.  # noqa: E501

        :param frame: The frame of this Box.  # noqa: E501
        :type: int
        """

        self._frame = frame

    @property
    def attributes(self):
        """Gets the attributes of this Box.  # noqa: E501

        Object containing attribute values.  # noqa: E501

        :return: The attributes of this Box.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Box.

        Object containing attribute values.  # noqa: E501

        :param attributes: The attributes of this Box.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def x(self):
        """Gets the x of this Box.  # noqa: E501

        Normalized horizontal position of left edge of bounding box.  # noqa: E501

        :return: The x of this Box.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Box.

        Normalized horizontal position of left edge of bounding box.  # noqa: E501

        :param x: The x of this Box.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this Box.  # noqa: E501

        Normalized vertical position of top edge of bounding box.  # noqa: E501

        :return: The y of this Box.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Box.

        Normalized vertical position of top edge of bounding box.  # noqa: E501

        :param y: The y of this Box.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def width(self):
        """Gets the width of this Box.  # noqa: E501

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :return: The width of this Box.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Box.

        Normalized width of bounding box for `box` localization types.  # noqa: E501

        :param width: The width of this Box.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Box.  # noqa: E501

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :return: The height of this Box.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Box.

        Normalized height of bounding box for `box` localization types.  # noqa: E501

        :param height: The height of this Box.  # noqa: E501
        :type: float
        """

        self._height = height

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
        if issubclass(Box, dict):
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
        if not isinstance(other, Box):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other