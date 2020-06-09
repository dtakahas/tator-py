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


class AlgorithmLaunch(object):
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
        'group_id': 'str',
        'message': 'str',
        'run_uids': 'list[str]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'message': 'message',
        'run_uids': 'run_uids'
    }

    def __init__(self, group_id=None, message=None, run_uids=None, local_vars_configuration=None):  # noqa: E501
        """AlgorithmLaunch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_id = None
        self._message = None
        self._run_uids = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if message is not None:
            self.message = message
        if run_uids is not None:
            self.run_uids = run_uids

    @property
    def group_id(self):
        """Gets the group_id of this AlgorithmLaunch.  # noqa: E501

        A uuid1 string identifying the group of jobs started.  # noqa: E501

        :return: The group_id of this AlgorithmLaunch.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AlgorithmLaunch.

        A uuid1 string identifying the group of jobs started.  # noqa: E501

        :param group_id: The group_id of this AlgorithmLaunch.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def message(self):
        """Gets the message of this AlgorithmLaunch.  # noqa: E501

        Message indicating successful launch.  # noqa: E501

        :return: The message of this AlgorithmLaunch.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlgorithmLaunch.

        Message indicating successful launch.  # noqa: E501

        :param message: The message of this AlgorithmLaunch.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def run_uids(self):
        """Gets the run_uids of this AlgorithmLaunch.  # noqa: E501

        A list of uuid1 strings identifying each job started.  # noqa: E501

        :return: The run_uids of this AlgorithmLaunch.  # noqa: E501
        :rtype: list[str]
        """
        return self._run_uids

    @run_uids.setter
    def run_uids(self, run_uids):
        """Sets the run_uids of this AlgorithmLaunch.

        A list of uuid1 strings identifying each job started.  # noqa: E501

        :param run_uids: The run_uids of this AlgorithmLaunch.  # noqa: E501
        :type run_uids: list[str]
        """

        self._run_uids = run_uids

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
        if not isinstance(other, AlgorithmLaunch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlgorithmLaunch):
            return True

        return self.to_dict() != other.to_dict()