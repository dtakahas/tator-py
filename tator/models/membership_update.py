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


class MembershipUpdate(object):
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
        'permission': 'str'
    }

    attribute_map = {
        'permission': 'permission'
    }

    def __init__(self, permission=None, local_vars_configuration=None):  # noqa: E501
        """MembershipUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._permission = None
        self.discriminator = None

        if permission is not None:
            self.permission = permission

    @property
    def permission(self):
        """Gets the permission of this MembershipUpdate.  # noqa: E501

        User permission level for the project.  # noqa: E501

        :return: The permission of this MembershipUpdate.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this MembershipUpdate.

        User permission level for the project.  # noqa: E501

        :param permission: The permission of this MembershipUpdate.  # noqa: E501
        :type permission: str
        """
        allowed_values = ["View Only", "Can Edit", "Can Transfer", "Can Execute", "Full Control"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and permission not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

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
        if not isinstance(other, MembershipUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MembershipUpdate):
            return True

        return self.to_dict() != other.to_dict()
