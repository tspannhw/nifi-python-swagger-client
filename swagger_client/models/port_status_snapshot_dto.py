# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PortStatusSnapshotDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'id': 'str',
        'group_id': 'str',
        'name': 'str',
        'active_thread_count': 'int',
        'flow_files_in': 'int',
        'bytes_in': 'int',
        'input': 'str',
        'flow_files_out': 'int',
        'bytes_out': 'int',
        'output': 'str',
        'transmitting': 'bool',
        'run_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'name': 'name',
        'active_thread_count': 'activeThreadCount',
        'flow_files_in': 'flowFilesIn',
        'bytes_in': 'bytesIn',
        'input': 'input',
        'flow_files_out': 'flowFilesOut',
        'bytes_out': 'bytesOut',
        'output': 'output',
        'transmitting': 'transmitting',
        'run_status': 'runStatus'
    }

    def __init__(self, id=None, group_id=None, name=None, active_thread_count=None, flow_files_in=None, bytes_in=None, input=None, flow_files_out=None, bytes_out=None, output=None, transmitting=False, run_status=None):
        """
        PortStatusSnapshotDTO - a model defined in Swagger
        """

        self._id = None
        self._group_id = None
        self._name = None
        self._active_thread_count = None
        self._flow_files_in = None
        self._bytes_in = None
        self._input = None
        self._flow_files_out = None
        self._bytes_out = None
        self._output = None
        self._transmitting = None
        self._run_status = None

        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if name is not None:
          self.name = name
        if active_thread_count is not None:
          self.active_thread_count = active_thread_count
        if flow_files_in is not None:
          self.flow_files_in = flow_files_in
        if bytes_in is not None:
          self.bytes_in = bytes_in
        if input is not None:
          self.input = input
        if flow_files_out is not None:
          self.flow_files_out = flow_files_out
        if bytes_out is not None:
          self.bytes_out = bytes_out
        if output is not None:
          self.output = output
        if transmitting is not None:
          self.transmitting = transmitting
        if run_status is not None:
          self.run_status = run_status

    @property
    def id(self):
        """
        Gets the id of this PortStatusSnapshotDTO.
        The id of the port.

        :return: The id of this PortStatusSnapshotDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PortStatusSnapshotDTO.
        The id of the port.

        :param id: The id of this PortStatusSnapshotDTO.
        :type: str
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this PortStatusSnapshotDTO.
        The id of the parent process group of the port.

        :return: The group_id of this PortStatusSnapshotDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this PortStatusSnapshotDTO.
        The id of the parent process group of the port.

        :param group_id: The group_id of this PortStatusSnapshotDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this PortStatusSnapshotDTO.
        The name of the port.

        :return: The name of this PortStatusSnapshotDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PortStatusSnapshotDTO.
        The name of the port.

        :param name: The name of this PortStatusSnapshotDTO.
        :type: str
        """

        self._name = name

    @property
    def active_thread_count(self):
        """
        Gets the active_thread_count of this PortStatusSnapshotDTO.
        The active thread count for the port.

        :return: The active_thread_count of this PortStatusSnapshotDTO.
        :rtype: int
        """
        return self._active_thread_count

    @active_thread_count.setter
    def active_thread_count(self, active_thread_count):
        """
        Sets the active_thread_count of this PortStatusSnapshotDTO.
        The active thread count for the port.

        :param active_thread_count: The active_thread_count of this PortStatusSnapshotDTO.
        :type: int
        """

        self._active_thread_count = active_thread_count

    @property
    def flow_files_in(self):
        """
        Gets the flow_files_in of this PortStatusSnapshotDTO.
        The number of FlowFiles that have been accepted in the last 5 minutes.

        :return: The flow_files_in of this PortStatusSnapshotDTO.
        :rtype: int
        """
        return self._flow_files_in

    @flow_files_in.setter
    def flow_files_in(self, flow_files_in):
        """
        Sets the flow_files_in of this PortStatusSnapshotDTO.
        The number of FlowFiles that have been accepted in the last 5 minutes.

        :param flow_files_in: The flow_files_in of this PortStatusSnapshotDTO.
        :type: int
        """

        self._flow_files_in = flow_files_in

    @property
    def bytes_in(self):
        """
        Gets the bytes_in of this PortStatusSnapshotDTO.
        The size of hte FlowFiles that have been accepted in the last 5 minutes.

        :return: The bytes_in of this PortStatusSnapshotDTO.
        :rtype: int
        """
        return self._bytes_in

    @bytes_in.setter
    def bytes_in(self, bytes_in):
        """
        Sets the bytes_in of this PortStatusSnapshotDTO.
        The size of hte FlowFiles that have been accepted in the last 5 minutes.

        :param bytes_in: The bytes_in of this PortStatusSnapshotDTO.
        :type: int
        """

        self._bytes_in = bytes_in

    @property
    def input(self):
        """
        Gets the input of this PortStatusSnapshotDTO.
        The count/size of flowfiles that have been accepted in the last 5 minutes.

        :return: The input of this PortStatusSnapshotDTO.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this PortStatusSnapshotDTO.
        The count/size of flowfiles that have been accepted in the last 5 minutes.

        :param input: The input of this PortStatusSnapshotDTO.
        :type: str
        """

        self._input = input

    @property
    def flow_files_out(self):
        """
        Gets the flow_files_out of this PortStatusSnapshotDTO.
        The number of FlowFiles that have been processed in the last 5 minutes.

        :return: The flow_files_out of this PortStatusSnapshotDTO.
        :rtype: int
        """
        return self._flow_files_out

    @flow_files_out.setter
    def flow_files_out(self, flow_files_out):
        """
        Sets the flow_files_out of this PortStatusSnapshotDTO.
        The number of FlowFiles that have been processed in the last 5 minutes.

        :param flow_files_out: The flow_files_out of this PortStatusSnapshotDTO.
        :type: int
        """

        self._flow_files_out = flow_files_out

    @property
    def bytes_out(self):
        """
        Gets the bytes_out of this PortStatusSnapshotDTO.
        The number of bytes that have been processed in the last 5 minutes.

        :return: The bytes_out of this PortStatusSnapshotDTO.
        :rtype: int
        """
        return self._bytes_out

    @bytes_out.setter
    def bytes_out(self, bytes_out):
        """
        Sets the bytes_out of this PortStatusSnapshotDTO.
        The number of bytes that have been processed in the last 5 minutes.

        :param bytes_out: The bytes_out of this PortStatusSnapshotDTO.
        :type: int
        """

        self._bytes_out = bytes_out

    @property
    def output(self):
        """
        Gets the output of this PortStatusSnapshotDTO.
        The count/size of flowfiles that have been processed in the last 5 minutes.

        :return: The output of this PortStatusSnapshotDTO.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this PortStatusSnapshotDTO.
        The count/size of flowfiles that have been processed in the last 5 minutes.

        :param output: The output of this PortStatusSnapshotDTO.
        :type: str
        """

        self._output = output

    @property
    def transmitting(self):
        """
        Gets the transmitting of this PortStatusSnapshotDTO.
        Whether the port has incoming or outgoing connections to a remote NiFi.

        :return: The transmitting of this PortStatusSnapshotDTO.
        :rtype: bool
        """
        return self._transmitting

    @transmitting.setter
    def transmitting(self, transmitting):
        """
        Sets the transmitting of this PortStatusSnapshotDTO.
        Whether the port has incoming or outgoing connections to a remote NiFi.

        :param transmitting: The transmitting of this PortStatusSnapshotDTO.
        :type: bool
        """

        self._transmitting = transmitting

    @property
    def run_status(self):
        """
        Gets the run_status of this PortStatusSnapshotDTO.
        The run status of the port.

        :return: The run_status of this PortStatusSnapshotDTO.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """
        Sets the run_status of this PortStatusSnapshotDTO.
        The run status of the port.

        :param run_status: The run_status of this PortStatusSnapshotDTO.
        :type: str
        """

        self._run_status = run_status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PortStatusSnapshotDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
