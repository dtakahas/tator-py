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


class Version(object):
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
        'bases': 'list[int]',
        'created_by': 'str',
        'created_datetime': 'str',
        'description': 'str',
        'id': 'int',
        'modified_by': 'str',
        'modified_datetime': 'str',
        'name': 'str',
        'num_created': 'int',
        'num_modified': 'int',
        'number': 'int',
        'project': 'int',
        'show_empty': 'bool'
    }

    attribute_map = {
        'bases': 'bases',
        'created_by': 'created_by',
        'created_datetime': 'created_datetime',
        'description': 'description',
        'id': 'id',
        'modified_by': 'modified_by',
        'modified_datetime': 'modified_datetime',
        'name': 'name',
        'num_created': 'num_created',
        'num_modified': 'num_modified',
        'number': 'number',
        'project': 'project',
        'show_empty': 'show_empty'
    }

    def __init__(self, bases=None, created_by=None, created_datetime=None, description='', id=None, modified_by=None, modified_datetime=None, name=None, num_created=None, num_modified=None, number=None, project=None, show_empty=True, local_vars_configuration=None):  # noqa: E501
        """Version - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bases = None
        self._created_by = None
        self._created_datetime = None
        self._description = None
        self._id = None
        self._modified_by = None
        self._modified_datetime = None
        self._name = None
        self._num_created = None
        self._num_modified = None
        self._number = None
        self._project = None
        self._show_empty = None
        self.discriminator = None

        if bases is not None:
            self.bases = bases
        if created_by is not None:
            self.created_by = created_by
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_datetime is not None:
            self.modified_datetime = modified_datetime
        if name is not None:
            self.name = name
        if num_created is not None:
            self.num_created = num_created
        if num_modified is not None:
            self.num_modified = num_modified
        if number is not None:
            self.number = number
        if project is not None:
            self.project = project
        if show_empty is not None:
            self.show_empty = show_empty

    @property
    def bases(self):
        """Gets the bases of this Version.  # noqa: E501

        Array of other version IDs that are dependencies of this version.  # noqa: E501

        :return: The bases of this Version.  # noqa: E501
        :rtype: list[int]
        """
        return self._bases

    @bases.setter
    def bases(self, bases):
        """Sets the bases of this Version.

        Array of other version IDs that are dependencies of this version.  # noqa: E501

        :param bases: The bases of this Version.  # noqa: E501
        :type: list[int]
        """

        self._bases = bases

    @property
    def created_by(self):
        """Gets the created_by of this Version.  # noqa: E501

        Name of user who created the last unmodified annotation in this version.  # noqa: E501

        :return: The created_by of this Version.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Version.

        Name of user who created the last unmodified annotation in this version.  # noqa: E501

        :param created_by: The created_by of this Version.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_datetime(self):
        """Gets the created_datetime of this Version.  # noqa: E501

        Datetime when the last unmodified annotation was created.  # noqa: E501

        :return: The created_datetime of this Version.  # noqa: E501
        :rtype: str
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this Version.

        Datetime when the last unmodified annotation was created.  # noqa: E501

        :param created_datetime: The created_datetime of this Version.  # noqa: E501
        :type: str
        """

        self._created_datetime = created_datetime

    @property
    def description(self):
        """Gets the description of this Version.  # noqa: E501

        Description of the version.  # noqa: E501

        :return: The description of this Version.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Version.

        Description of the version.  # noqa: E501

        :param description: The description of this Version.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Version.  # noqa: E501

        Unique integer identifying a membership.  # noqa: E501

        :return: The id of this Version.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.

        Unique integer identifying a membership.  # noqa: E501

        :param id: The id of this Version.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def modified_by(self):
        """Gets the modified_by of this Version.  # noqa: E501

        Name of user who modified annotations in this version most recently.  # noqa: E501

        :return: The modified_by of this Version.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Version.

        Name of user who modified annotations in this version most recently.  # noqa: E501

        :param modified_by: The modified_by of this Version.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_datetime(self):
        """Gets the modified_datetime of this Version.  # noqa: E501

        Datetime when last annotation was modified in the web interface.  # noqa: E501

        :return: The modified_datetime of this Version.  # noqa: E501
        :rtype: str
        """
        return self._modified_datetime

    @modified_datetime.setter
    def modified_datetime(self, modified_datetime):
        """Sets the modified_datetime of this Version.

        Datetime when last annotation was modified in the web interface.  # noqa: E501

        :param modified_datetime: The modified_datetime of this Version.  # noqa: E501
        :type: str
        """

        self._modified_datetime = modified_datetime

    @property
    def name(self):
        """Gets the name of this Version.  # noqa: E501

        Name of the version.  # noqa: E501

        :return: The name of this Version.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Version.

        Name of the version.  # noqa: E501

        :param name: The name of this Version.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_created(self):
        """Gets the num_created of this Version.  # noqa: E501

        Number of created annotations in this version.  # noqa: E501

        :return: The num_created of this Version.  # noqa: E501
        :rtype: int
        """
        return self._num_created

    @num_created.setter
    def num_created(self, num_created):
        """Sets the num_created of this Version.

        Number of created annotations in this version.  # noqa: E501

        :param num_created: The num_created of this Version.  # noqa: E501
        :type: int
        """

        self._num_created = num_created

    @property
    def num_modified(self):
        """Gets the num_modified of this Version.  # noqa: E501

        Number of modified annotations in this version.  # noqa: E501

        :return: The num_modified of this Version.  # noqa: E501
        :rtype: int
        """
        return self._num_modified

    @num_modified.setter
    def num_modified(self, num_modified):
        """Sets the num_modified of this Version.

        Number of modified annotations in this version.  # noqa: E501

        :param num_modified: The num_modified of this Version.  # noqa: E501
        :type: int
        """

        self._num_modified = num_modified

    @property
    def number(self):
        """Gets the number of this Version.  # noqa: E501

        Version number.  # noqa: E501

        :return: The number of this Version.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Version.

        Version number.  # noqa: E501

        :param number: The number of this Version.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def project(self):
        """Gets the project of this Version.  # noqa: E501

        Unique integer identifying a project.  # noqa: E501

        :return: The project of this Version.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Version.

        Unique integer identifying a project.  # noqa: E501

        :param project: The project of this Version.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def show_empty(self):
        """Gets the show_empty of this Version.  # noqa: E501

        Whether to show this version on media for which no annotations exist.  # noqa: E501

        :return: The show_empty of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._show_empty

    @show_empty.setter
    def show_empty(self, show_empty):
        """Sets the show_empty of this Version.

        Whether to show this version on media for which no annotations exist.  # noqa: E501

        :param show_empty: The show_empty of this Version.  # noqa: E501
        :type: bool
        """

        self._show_empty = show_empty

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
        if not isinstance(other, Version):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Version):
            return True

        return self.to_dict() != other.to_dict()
