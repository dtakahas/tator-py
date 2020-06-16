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


class ProgressSpec(object):
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
        'job_type': 'str',
        'media_ids': 'str',
        'message': 'str',
        'name': 'str',
        'progress': 'float',
        'section': 'str',
        'sections': 'str',
        'state': 'str',
        'swid': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'job_type': 'job_type',
        'media_ids': 'media_ids',
        'message': 'message',
        'name': 'name',
        'progress': 'progress',
        'section': 'section',
        'sections': 'sections',
        'state': 'state',
        'swid': 'swid',
        'uid': 'uid'
    }

    def __init__(self, gid=None, job_type=None, media_ids=None, message=None, name=None, progress=None, section=None, sections=None, state=None, swid=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """ProgressSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._job_type = None
        self._media_ids = None
        self._message = None
        self._name = None
        self._progress = None
        self._section = None
        self._sections = None
        self._state = None
        self._swid = None
        self._uid = None
        self.discriminator = None

        self.gid = gid
        self.job_type = job_type
        if media_ids is not None:
            self.media_ids = media_ids
        self.message = message
        self.name = name
        self.progress = progress
        if section is not None:
            self.section = section
        if sections is not None:
            self.sections = sections
        self.state = state
        if swid is not None:
            self.swid = swid
        self.uid = uid

    @property
    def gid(self):
        """Gets the gid of this ProgressSpec.  # noqa: E501

        UUID generated for the job group. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :return: The gid of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProgressSpec.

        UUID generated for the job group. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :param gid: The gid of this ProgressSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and gid is None:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501

        self._gid = gid

    @property
    def job_type(self):
        """Gets the job_type of this ProgressSpec.  # noqa: E501

        Type of background job.  # noqa: E501

        :return: The job_type of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ProgressSpec.

        Type of background job.  # noqa: E501

        :param job_type: The job_type of this ProgressSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and job_type is None:  # noqa: E501
            raise ValueError("Invalid value for `job_type`, must not be `None`")  # noqa: E501
        allowed_values = ["upload", "download", "algorithm"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and job_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `job_type` ({0}), must be one of {1}"  # noqa: E501
                .format(job_type, allowed_values)
            )

        self._job_type = job_type

    @property
    def media_ids(self):
        """Gets the media_ids of this ProgressSpec.  # noqa: E501

        Comma separated string of media ids, one for each media that this job applies to. Required only for `job_type` of `algorithm`.  # noqa: E501

        :return: The media_ids of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._media_ids

    @media_ids.setter
    def media_ids(self, media_ids):
        """Sets the media_ids of this ProgressSpec.

        Comma separated string of media ids, one for each media that this job applies to. Required only for `job_type` of `algorithm`.  # noqa: E501

        :param media_ids: The media_ids of this ProgressSpec.  # noqa: E501
        :type: str
        """

        self._media_ids = media_ids

    @property
    def message(self):
        """Gets the message of this ProgressSpec.  # noqa: E501

        Progress message. This should be short to fit in the UI.  # noqa: E501

        :return: The message of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProgressSpec.

        Progress message. This should be short to fit in the UI.  # noqa: E501

        :param message: The message of this ProgressSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def name(self):
        """Gets the name of this ProgressSpec.  # noqa: E501

        Name of the job.  # noqa: E501

        :return: The name of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProgressSpec.

        Name of the job.  # noqa: E501

        :param name: The name of this ProgressSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def progress(self):
        """Gets the progress of this ProgressSpec.  # noqa: E501

        Progress percent completion. This is used to display the progress bar associated with the job.  # noqa: E501

        :return: The progress of this ProgressSpec.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ProgressSpec.

        Progress percent completion. This is used to display the progress bar associated with the job.  # noqa: E501

        :param progress: The progress of this ProgressSpec.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and progress is None:  # noqa: E501
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and progress > 100):  # noqa: E501
            raise ValueError("Invalid value for `progress`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and progress < 0):  # noqa: E501
            raise ValueError("Invalid value for `progress`, must be a value greater than or equal to `0`")  # noqa: E501

        self._progress = progress

    @property
    def section(self):
        """Gets the section of this ProgressSpec.  # noqa: E501

        Media section name. Required only for `job_type` of `upload`.  # noqa: E501

        :return: The section of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this ProgressSpec.

        Media section name. Required only for `job_type` of `upload`.  # noqa: E501

        :param section: The section of this ProgressSpec.  # noqa: E501
        :type: str
        """

        self._section = section

    @property
    def sections(self):
        """Gets the sections of this ProgressSpec.  # noqa: E501

        Comma separated string of media sections, one for each media ID that this job applies to. Required only for `job_type` of `algorithm`.  # noqa: E501

        :return: The sections of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this ProgressSpec.

        Comma separated string of media sections, one for each media ID that this job applies to. Required only for `job_type` of `algorithm`.  # noqa: E501

        :param sections: The sections of this ProgressSpec.  # noqa: E501
        :type: str
        """

        self._sections = sections

    @property
    def state(self):
        """Gets the state of this ProgressSpec.  # noqa: E501

        State of the job.  # noqa: E501

        :return: The state of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProgressSpec.

        State of the job.  # noqa: E501

        :param state: The state of this ProgressSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["queued", "started", "failed", "finished"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def swid(self):
        """Gets the swid of this ProgressSpec.  # noqa: E501

        UUID generated for the service worker that is doing an upload. This field is required if the `job_type` is `upload`.  # noqa: E501

        :return: The swid of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._swid

    @swid.setter
    def swid(self, swid):
        """Sets the swid of this ProgressSpec.

        UUID generated for the service worker that is doing an upload. This field is required if the `job_type` is `upload`.  # noqa: E501

        :param swid: The swid of this ProgressSpec.  # noqa: E501
        :type: str
        """

        self._swid = swid

    @property
    def uid(self):
        """Gets the uid of this ProgressSpec.  # noqa: E501

        UUID generated for the individual job. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :return: The uid of this ProgressSpec.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ProgressSpec.

        UUID generated for the individual job. This value is returned in the response of the `AlgorithmLaunch` and `Transcode` endpoints.  # noqa: E501

        :param uid: The uid of this ProgressSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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
        if not isinstance(other, ProgressSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProgressSpec):
            return True

        return self.to_dict() != other.to_dict()
