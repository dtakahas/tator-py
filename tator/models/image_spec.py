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


class ImageSpec(object):
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
        'gid': 'str',
        'md5': 'str',
        'name': 'str',
        'section': 'str',
        'thumbnail_url': 'str',
        'type': 'int',
        'uid': 'str',
        'url': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'md5': 'md5',
        'name': 'name',
        'section': 'section',
        'thumbnail_url': 'thumbnail_url',
        'type': 'type',
        'uid': 'uid',
        'url': 'url'
    }

    def __init__(self, gid=None, md5=None, name=None, section=None, thumbnail_url=None, type=None, uid=None, url=None, local_vars_configuration=None):  # noqa: E501
        """ImageSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._md5 = None
        self._name = None
        self._section = None
        self._thumbnail_url = None
        self._type = None
        self._uid = None
        self._url = None
        self.discriminator = None

        self.gid = gid
        self.md5 = md5
        self.name = name
        self.section = section
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        self.type = type
        self.uid = uid
        self.url = url

    @property
    def gid(self):
        """Gets the gid of this ImageSpec.  # noqa: E501

        UUID generated for the job group. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :return: The gid of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ImageSpec.

        UUID generated for the job group. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :param gid: The gid of this ImageSpec.  # noqa: E501
        :type gid: str
        """
        if self.local_vars_configuration.client_side_validation and gid is None:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501

        self._gid = gid

    @property
    def md5(self):
        """Gets the md5 of this ImageSpec.  # noqa: E501

        MD5 sum of the media file.  # noqa: E501

        :return: The md5 of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this ImageSpec.

        MD5 sum of the media file.  # noqa: E501

        :param md5: The md5 of this ImageSpec.  # noqa: E501
        :type md5: str
        """
        if self.local_vars_configuration.client_side_validation and md5 is None:  # noqa: E501
            raise ValueError("Invalid value for `md5`, must not be `None`")  # noqa: E501

        self._md5 = md5

    @property
    def name(self):
        """Gets the name of this ImageSpec.  # noqa: E501

        Name of the file.  # noqa: E501

        :return: The name of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageSpec.

        Name of the file.  # noqa: E501

        :param name: The name of this ImageSpec.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def section(self):
        """Gets the section of this ImageSpec.  # noqa: E501

        Media section name.  # noqa: E501

        :return: The section of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this ImageSpec.

        Media section name.  # noqa: E501

        :param section: The section of this ImageSpec.  # noqa: E501
        :type section: str
        """
        if self.local_vars_configuration.client_side_validation and section is None:  # noqa: E501
            raise ValueError("Invalid value for `section`, must not be `None`")  # noqa: E501

        self._section = section

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this ImageSpec.  # noqa: E501

        Upload URL for the thumbnail if already generated.  # noqa: E501

        :return: The thumbnail_url of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this ImageSpec.

        Upload URL for the thumbnail if already generated.  # noqa: E501

        :param thumbnail_url: The thumbnail_url of this ImageSpec.  # noqa: E501
        :type thumbnail_url: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def type(self):
        """Gets the type of this ImageSpec.  # noqa: E501

        Unique integer identifying an image type. Use -1 to automatically select the image type if only one image type exists in a project.  # noqa: E501

        :return: The type of this ImageSpec.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageSpec.

        Unique integer identifying an image type. Use -1 to automatically select the image type if only one image type exists in a project.  # noqa: E501

        :param type: The type of this ImageSpec.  # noqa: E501
        :type type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and type < -1):  # noqa: E501
            raise ValueError("Invalid value for `type`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this ImageSpec.  # noqa: E501

        UUID generated for the individual job. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :return: The uid of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ImageSpec.

        UUID generated for the individual job. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :param uid: The uid of this ImageSpec.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def url(self):
        """Gets the url of this ImageSpec.  # noqa: E501

        Upload URL for the image.  # noqa: E501

        :return: The url of this ImageSpec.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageSpec.

        Upload URL for the image.  # noqa: E501

        :param url: The url of this ImageSpec.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, ImageSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageSpec):
            return True

        return self.to_dict() != other.to_dict()
