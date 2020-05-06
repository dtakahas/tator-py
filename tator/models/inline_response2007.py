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


class InlineResponse2007(object):
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
        'permission': 'str',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'username': 'username'
    }

    def __init__(self, id=None, permission=None, username=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._permission = None
        self._username = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if username is not None:
            self.username = username

    @property
    def id(self):
        """Gets the id of this InlineResponse2007.  # noqa: E501

        Unique integer identifying a membership.  # noqa: E501

        :return: The id of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2007.

        Unique integer identifying a membership.  # noqa: E501

        :param id: The id of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def permission(self):
        """Gets the permission of this InlineResponse2007.  # noqa: E501

        User permission level for the project.  # noqa: E501

        :return: The permission of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this InlineResponse2007.

        User permission level for the project.  # noqa: E501

        :param permission: The permission of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        allowed_values = ["view_only", "can_edit", "can_transfer", "can_execute", "full_control"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def username(self):
        """Gets the username of this InlineResponse2007.  # noqa: E501

        Username for the membership.  # noqa: E501

        :return: The username of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineResponse2007.

        Username for the membership.  # noqa: E501

        :param username: The username of this InlineResponse2007.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
