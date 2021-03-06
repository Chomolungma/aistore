# coding: utf-8

"""
    AIS

    AIS is a scalable object-storage based caching system with Amazon and Google Cloud backends.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: dfcdev@exchange.nvidia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DaemonCoreStatistics(object):
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
        'numget': 'int',
        'numput': 'int',
        'numpost': 'int',
        'numdelete': 'int',
        'numrename': 'int',
        'numlist': 'int',
        'getlatency': 'int',
        'putlatency': 'int',
        'listlatency': 'int',
        'numerr': 'int'
    }

    attribute_map = {
        'numget': 'numget',
        'numput': 'numput',
        'numpost': 'numpost',
        'numdelete': 'numdelete',
        'numrename': 'numrename',
        'numlist': 'numlist',
        'getlatency': 'getlatency',
        'putlatency': 'putlatency',
        'listlatency': 'listlatency',
        'numerr': 'numerr'
    }

    def __init__(self, numget=None, numput=None, numpost=None, numdelete=None, numrename=None, numlist=None, getlatency=None, putlatency=None, listlatency=None, numerr=None):  # noqa: E501
        """DaemonCoreStatistics - a model defined in OpenAPI"""  # noqa: E501

        self._numget = None
        self._numput = None
        self._numpost = None
        self._numdelete = None
        self._numrename = None
        self._numlist = None
        self._getlatency = None
        self._putlatency = None
        self._listlatency = None
        self._numerr = None
        self.discriminator = None

        if numget is not None:
            self.numget = numget
        if numput is not None:
            self.numput = numput
        if numpost is not None:
            self.numpost = numpost
        if numdelete is not None:
            self.numdelete = numdelete
        if numrename is not None:
            self.numrename = numrename
        if numlist is not None:
            self.numlist = numlist
        if getlatency is not None:
            self.getlatency = getlatency
        if putlatency is not None:
            self.putlatency = putlatency
        if listlatency is not None:
            self.listlatency = listlatency
        if numerr is not None:
            self.numerr = numerr

    @property
    def numget(self):
        """Gets the numget of this DaemonCoreStatistics.  # noqa: E501


        :return: The numget of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numget

    @numget.setter
    def numget(self, numget):
        """Sets the numget of this DaemonCoreStatistics.


        :param numget: The numget of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numget = numget

    @property
    def numput(self):
        """Gets the numput of this DaemonCoreStatistics.  # noqa: E501


        :return: The numput of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numput

    @numput.setter
    def numput(self, numput):
        """Sets the numput of this DaemonCoreStatistics.


        :param numput: The numput of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numput = numput

    @property
    def numpost(self):
        """Gets the numpost of this DaemonCoreStatistics.  # noqa: E501


        :return: The numpost of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numpost

    @numpost.setter
    def numpost(self, numpost):
        """Sets the numpost of this DaemonCoreStatistics.


        :param numpost: The numpost of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numpost = numpost

    @property
    def numdelete(self):
        """Gets the numdelete of this DaemonCoreStatistics.  # noqa: E501


        :return: The numdelete of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numdelete

    @numdelete.setter
    def numdelete(self, numdelete):
        """Sets the numdelete of this DaemonCoreStatistics.


        :param numdelete: The numdelete of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numdelete = numdelete

    @property
    def numrename(self):
        """Gets the numrename of this DaemonCoreStatistics.  # noqa: E501


        :return: The numrename of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numrename

    @numrename.setter
    def numrename(self, numrename):
        """Sets the numrename of this DaemonCoreStatistics.


        :param numrename: The numrename of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numrename = numrename

    @property
    def numlist(self):
        """Gets the numlist of this DaemonCoreStatistics.  # noqa: E501


        :return: The numlist of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numlist

    @numlist.setter
    def numlist(self, numlist):
        """Sets the numlist of this DaemonCoreStatistics.


        :param numlist: The numlist of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numlist = numlist

    @property
    def getlatency(self):
        """Gets the getlatency of this DaemonCoreStatistics.  # noqa: E501


        :return: The getlatency of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._getlatency

    @getlatency.setter
    def getlatency(self, getlatency):
        """Sets the getlatency of this DaemonCoreStatistics.


        :param getlatency: The getlatency of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._getlatency = getlatency

    @property
    def putlatency(self):
        """Gets the putlatency of this DaemonCoreStatistics.  # noqa: E501


        :return: The putlatency of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._putlatency

    @putlatency.setter
    def putlatency(self, putlatency):
        """Sets the putlatency of this DaemonCoreStatistics.


        :param putlatency: The putlatency of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._putlatency = putlatency

    @property
    def listlatency(self):
        """Gets the listlatency of this DaemonCoreStatistics.  # noqa: E501


        :return: The listlatency of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._listlatency

    @listlatency.setter
    def listlatency(self, listlatency):
        """Sets the listlatency of this DaemonCoreStatistics.


        :param listlatency: The listlatency of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._listlatency = listlatency

    @property
    def numerr(self):
        """Gets the numerr of this DaemonCoreStatistics.  # noqa: E501


        :return: The numerr of this DaemonCoreStatistics.  # noqa: E501
        :rtype: int
        """
        return self._numerr

    @numerr.setter
    def numerr(self, numerr):
        """Sets the numerr of this DaemonCoreStatistics.


        :param numerr: The numerr of this DaemonCoreStatistics.  # noqa: E501
        :type: int
        """

        self._numerr = numerr

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
        if not isinstance(other, DaemonCoreStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
