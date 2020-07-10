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


class EncodeConfig(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'crf': 'int',
        'preset': 'str',
        'tune': 'str',
        'vcodec': 'str'
    }

    attribute_map = {
        'crf': 'crf',
        'preset': 'preset',
        'tune': 'tune',
        'vcodec': 'vcodec'
    }

    def __init__(self, crf=23, preset='fast', tune='fastdecode', vcodec='libx265', local_vars_configuration=None):  # noqa: E501
        """EncodeConfig - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._crf = None
        self._preset = None
        self._tune = None
        self._vcodec = None
        self.discriminator = None

        if crf is not None:
            self.crf = crf
        if preset is not None:
            self.preset = preset
        if tune is not None:
            self.tune = tune
        if vcodec is not None:
            self.vcodec = vcodec

    @property
    def crf(self):
        """
        Constant rate factor.

        :return: The crf of this EncodeConfig. 
        :rtype: int
        """
        return self._crf

    @crf.setter
    def crf(self, crf):
        """
        Constant rate factor.

        :param crf: The crf of this EncodeConfig.
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                crf is not None and crf > 51):  # noqa: E501
            raise ValueError("Invalid value for `crf`, must be a value less than or equal to `51`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                crf is not None and crf < 0):  # noqa: E501
            raise ValueError("Invalid value for `crf`, must be a value greater than or equal to `0`")  # noqa: E501

        self._crf = crf

    @property
    def preset(self):
        """
        Preset for ffmpeg encoding.

        :return: The preset of this EncodeConfig. 
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """
        Preset for ffmpeg encoding.

        :param preset: The preset of this EncodeConfig.
        :type: str
        """
        allowed_values = ["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and preset not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `preset` ({0}), must be one of {1}"  # noqa: E501
                .format(preset, allowed_values)
            )

        self._preset = preset

    @property
    def tune(self):
        """
        Tune setting for ffmpeg.

        :return: The tune of this EncodeConfig. 
        :rtype: str
        """
        return self._tune

    @tune.setter
    def tune(self, tune):
        """
        Tune setting for ffmpeg.

        :param tune: The tune of this EncodeConfig.
        :type: str
        """
        allowed_values = ["film", "animation", "grain", "stillimage", "fastdecode", "zerolatency", "psnr", "ssim"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tune not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tune` ({0}), must be one of {1}"  # noqa: E501
                .format(tune, allowed_values)
            )

        self._tune = tune

    @property
    def vcodec(self):
        """
        Video codec.

        :return: The vcodec of this EncodeConfig. 
        :rtype: str
        """
        return self._vcodec

    @vcodec.setter
    def vcodec(self, vcodec):
        """
        Video codec.

        :param vcodec: The vcodec of this EncodeConfig.
        :type: str
        """
        allowed_values = ["libx264", "libx265"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and vcodec not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `vcodec` ({0}), must be one of {1}"  # noqa: E501
                .format(vcodec, allowed_values)
            )

        self._vcodec = vcodec

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
        if not isinstance(other, EncodeConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncodeConfig):
            return True

        return self.to_dict() != other.to_dict()
