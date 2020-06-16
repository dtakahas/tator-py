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


class StateType(object):
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
        'association': 'str',
        'attribute_types': 'list[AttributeType]',
        'description': 'str',
        'dtype': 'str',
        'id': 'int',
        'interpolation': 'str',
        'media': 'list[int]',
        'name': 'str',
        'project': 'int',
        'visible': 'bool'
    }

    attribute_map = {
        'association': 'association',
        'attribute_types': 'attribute_types',
        'description': 'description',
        'dtype': 'dtype',
        'id': 'id',
        'interpolation': 'interpolation',
        'media': 'media',
        'name': 'name',
        'project': 'project',
        'visible': 'visible'
    }

    def __init__(self, association=None, attribute_types=None, description=None, dtype=None, id=None, interpolation='latest', media=None, name=None, project=None, visible=None, local_vars_configuration=None):  # noqa: E501
        """StateType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._association = None
        self._attribute_types = None
        self._description = None
        self._dtype = None
        self._id = None
        self._interpolation = None
        self._media = None
        self._name = None
        self._project = None
        self._visible = None
        self.discriminator = None

        if association is not None:
            self.association = association
        if attribute_types is not None:
            self.attribute_types = attribute_types
        if description is not None:
            self.description = description
        if dtype is not None:
            self.dtype = dtype
        if id is not None:
            self.id = id
        if interpolation is not None:
            self.interpolation = interpolation
        if media is not None:
            self.media = media
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if visible is not None:
            self.visible = visible

    @property
    def association(self):
        """Gets the association of this StateType.  # noqa: E501

        Type of object this state type is associated with.  # noqa: E501

        :return: The association of this StateType.  # noqa: E501
        :rtype: str
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this StateType.

        Type of object this state type is associated with.  # noqa: E501

        :param association: The association of this StateType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Media", "Frame", "Localization"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and association not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `association` ({0}), must be one of {1}"  # noqa: E501
                .format(association, allowed_values)
            )

        self._association = association

    @property
    def attribute_types(self):
        """Gets the attribute_types of this StateType.  # noqa: E501

        Attribute type definitions.  # noqa: E501

        :return: The attribute_types of this StateType.  # noqa: E501
        :rtype: list[AttributeType]
        """
        return self._attribute_types

    @attribute_types.setter
    def attribute_types(self, attribute_types):
        """Sets the attribute_types of this StateType.

        Attribute type definitions.  # noqa: E501

        :param attribute_types: The attribute_types of this StateType.  # noqa: E501
        :type: list[AttributeType]
        """

        self._attribute_types = attribute_types

    @property
    def description(self):
        """Gets the description of this StateType.  # noqa: E501

        Description of the state type.  # noqa: E501

        :return: The description of this StateType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StateType.

        Description of the state type.  # noqa: E501

        :param description: The description of this StateType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dtype(self):
        """Gets the dtype of this StateType.  # noqa: E501

        String indicating data type. Always equal to \"state\".  # noqa: E501

        :return: The dtype of this StateType.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this StateType.

        String indicating data type. Always equal to \"state\".  # noqa: E501

        :param dtype: The dtype of this StateType.  # noqa: E501
        :type: str
        """

        self._dtype = dtype

    @property
    def id(self):
        """Gets the id of this StateType.  # noqa: E501

        Unique integer identifying a state type.  # noqa: E501

        :return: The id of this StateType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StateType.

        Unique integer identifying a state type.  # noqa: E501

        :param id: The id of this StateType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interpolation(self):
        """Gets the interpolation of this StateType.  # noqa: E501

        Interpolation method used by the web interface.  # noqa: E501

        :return: The interpolation of this StateType.  # noqa: E501
        :rtype: str
        """
        return self._interpolation

    @interpolation.setter
    def interpolation(self, interpolation):
        """Sets the interpolation of this StateType.

        Interpolation method used by the web interface.  # noqa: E501

        :param interpolation: The interpolation of this StateType.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "latest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and interpolation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `interpolation` ({0}), must be one of {1}"  # noqa: E501
                .format(interpolation, allowed_values)
            )

        self._interpolation = interpolation

    @property
    def media(self):
        """Gets the media of this StateType.  # noqa: E501

        List of integers identifying media types that this state type may apply to.  # noqa: E501

        :return: The media of this StateType.  # noqa: E501
        :rtype: list[int]
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this StateType.

        List of integers identifying media types that this state type may apply to.  # noqa: E501

        :param media: The media of this StateType.  # noqa: E501
        :type: list[int]
        """

        self._media = media

    @property
    def name(self):
        """Gets the name of this StateType.  # noqa: E501

        Name of the state type.  # noqa: E501

        :return: The name of this StateType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StateType.

        Name of the state type.  # noqa: E501

        :param name: The name of this StateType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this StateType.  # noqa: E501

        Unique integer identifying project for this state type.  # noqa: E501

        :return: The project of this StateType.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this StateType.

        Unique integer identifying project for this state type.  # noqa: E501

        :param project: The project of this StateType.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def visible(self):
        """Gets the visible of this StateType.  # noqa: E501

        Whether this state type should be displayed.  # noqa: E501

        :return: The visible of this StateType.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this StateType.

        Whether this state type should be displayed.  # noqa: E501

        :param visible: The visible of this StateType.  # noqa: E501
        :type: bool
        """

        self._visible = visible

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
        if not isinstance(other, StateType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StateType):
            return True

        return self.to_dict() != other.to_dict()
