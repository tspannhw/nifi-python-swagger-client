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


class DropRequestDTO(object):
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
        'uri': 'str',
        'submission_time': 'str',
        'last_updated': 'str',
        'percent_completed': 'int',
        'finished': 'bool',
        'failure_reason': 'str',
        'current_count': 'int',
        'current_size': 'int',
        'current': 'str',
        'original_count': 'int',
        'original_size': 'int',
        'original': 'str',
        'dropped_count': 'int',
        'dropped_size': 'int',
        'dropped': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'submission_time': 'submissionTime',
        'last_updated': 'lastUpdated',
        'percent_completed': 'percentCompleted',
        'finished': 'finished',
        'failure_reason': 'failureReason',
        'current_count': 'currentCount',
        'current_size': 'currentSize',
        'current': 'current',
        'original_count': 'originalCount',
        'original_size': 'originalSize',
        'original': 'original',
        'dropped_count': 'droppedCount',
        'dropped_size': 'droppedSize',
        'dropped': 'dropped',
        'state': 'state'
    }

    def __init__(self, id=None, uri=None, submission_time=None, last_updated=None, percent_completed=None, finished=False, failure_reason=None, current_count=None, current_size=None, current=None, original_count=None, original_size=None, original=None, dropped_count=None, dropped_size=None, dropped=None, state=None):
        """
        DropRequestDTO - a model defined in Swagger
        """

        self._id = None
        self._uri = None
        self._submission_time = None
        self._last_updated = None
        self._percent_completed = None
        self._finished = None
        self._failure_reason = None
        self._current_count = None
        self._current_size = None
        self._current = None
        self._original_count = None
        self._original_size = None
        self._original = None
        self._dropped_count = None
        self._dropped_size = None
        self._dropped = None
        self._state = None

        if id is not None:
          self.id = id
        if uri is not None:
          self.uri = uri
        if submission_time is not None:
          self.submission_time = submission_time
        if last_updated is not None:
          self.last_updated = last_updated
        if percent_completed is not None:
          self.percent_completed = percent_completed
        if finished is not None:
          self.finished = finished
        if failure_reason is not None:
          self.failure_reason = failure_reason
        if current_count is not None:
          self.current_count = current_count
        if current_size is not None:
          self.current_size = current_size
        if current is not None:
          self.current = current
        if original_count is not None:
          self.original_count = original_count
        if original_size is not None:
          self.original_size = original_size
        if original is not None:
          self.original = original
        if dropped_count is not None:
          self.dropped_count = dropped_count
        if dropped_size is not None:
          self.dropped_size = dropped_size
        if dropped is not None:
          self.dropped = dropped
        if state is not None:
          self.state = state

    @property
    def id(self):
        """
        Gets the id of this DropRequestDTO.
        The id for this drop request.

        :return: The id of this DropRequestDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DropRequestDTO.
        The id for this drop request.

        :param id: The id of this DropRequestDTO.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this DropRequestDTO.
        The URI for future requests to this drop request.

        :return: The uri of this DropRequestDTO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this DropRequestDTO.
        The URI for future requests to this drop request.

        :param uri: The uri of this DropRequestDTO.
        :type: str
        """

        self._uri = uri

    @property
    def submission_time(self):
        """
        Gets the submission_time of this DropRequestDTO.
        The timestamp when the query was submitted.

        :return: The submission_time of this DropRequestDTO.
        :rtype: str
        """
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        """
        Sets the submission_time of this DropRequestDTO.
        The timestamp when the query was submitted.

        :param submission_time: The submission_time of this DropRequestDTO.
        :type: str
        """

        self._submission_time = submission_time

    @property
    def last_updated(self):
        """
        Gets the last_updated of this DropRequestDTO.
        The last time this drop request was updated.

        :return: The last_updated of this DropRequestDTO.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this DropRequestDTO.
        The last time this drop request was updated.

        :param last_updated: The last_updated of this DropRequestDTO.
        :type: str
        """

        self._last_updated = last_updated

    @property
    def percent_completed(self):
        """
        Gets the percent_completed of this DropRequestDTO.
        The current percent complete.

        :return: The percent_completed of this DropRequestDTO.
        :rtype: int
        """
        return self._percent_completed

    @percent_completed.setter
    def percent_completed(self, percent_completed):
        """
        Sets the percent_completed of this DropRequestDTO.
        The current percent complete.

        :param percent_completed: The percent_completed of this DropRequestDTO.
        :type: int
        """

        self._percent_completed = percent_completed

    @property
    def finished(self):
        """
        Gets the finished of this DropRequestDTO.
        Whether the query has finished.

        :return: The finished of this DropRequestDTO.
        :rtype: bool
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished of this DropRequestDTO.
        Whether the query has finished.

        :param finished: The finished of this DropRequestDTO.
        :type: bool
        """

        self._finished = finished

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this DropRequestDTO.
        The reason, if any, that this drop request failed.

        :return: The failure_reason of this DropRequestDTO.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this DropRequestDTO.
        The reason, if any, that this drop request failed.

        :param failure_reason: The failure_reason of this DropRequestDTO.
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def current_count(self):
        """
        Gets the current_count of this DropRequestDTO.
        The number of flow files currently queued.

        :return: The current_count of this DropRequestDTO.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        """
        Sets the current_count of this DropRequestDTO.
        The number of flow files currently queued.

        :param current_count: The current_count of this DropRequestDTO.
        :type: int
        """

        self._current_count = current_count

    @property
    def current_size(self):
        """
        Gets the current_size of this DropRequestDTO.
        The size of flow files currently queued in bytes.

        :return: The current_size of this DropRequestDTO.
        :rtype: int
        """
        return self._current_size

    @current_size.setter
    def current_size(self, current_size):
        """
        Sets the current_size of this DropRequestDTO.
        The size of flow files currently queued in bytes.

        :param current_size: The current_size of this DropRequestDTO.
        :type: int
        """

        self._current_size = current_size

    @property
    def current(self):
        """
        Gets the current of this DropRequestDTO.
        The count and size of flow files currently queued.

        :return: The current of this DropRequestDTO.
        :rtype: str
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this DropRequestDTO.
        The count and size of flow files currently queued.

        :param current: The current of this DropRequestDTO.
        :type: str
        """

        self._current = current

    @property
    def original_count(self):
        """
        Gets the original_count of this DropRequestDTO.
        The number of flow files to be dropped as a result of this request.

        :return: The original_count of this DropRequestDTO.
        :rtype: int
        """
        return self._original_count

    @original_count.setter
    def original_count(self, original_count):
        """
        Sets the original_count of this DropRequestDTO.
        The number of flow files to be dropped as a result of this request.

        :param original_count: The original_count of this DropRequestDTO.
        :type: int
        """

        self._original_count = original_count

    @property
    def original_size(self):
        """
        Gets the original_size of this DropRequestDTO.
        The size of flow files to be dropped as a result of this request in bytes.

        :return: The original_size of this DropRequestDTO.
        :rtype: int
        """
        return self._original_size

    @original_size.setter
    def original_size(self, original_size):
        """
        Sets the original_size of this DropRequestDTO.
        The size of flow files to be dropped as a result of this request in bytes.

        :param original_size: The original_size of this DropRequestDTO.
        :type: int
        """

        self._original_size = original_size

    @property
    def original(self):
        """
        Gets the original of this DropRequestDTO.
        The count and size of flow files to be dropped as a result of this request.

        :return: The original of this DropRequestDTO.
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """
        Sets the original of this DropRequestDTO.
        The count and size of flow files to be dropped as a result of this request.

        :param original: The original of this DropRequestDTO.
        :type: str
        """

        self._original = original

    @property
    def dropped_count(self):
        """
        Gets the dropped_count of this DropRequestDTO.
        The number of flow files that have been dropped thus far.

        :return: The dropped_count of this DropRequestDTO.
        :rtype: int
        """
        return self._dropped_count

    @dropped_count.setter
    def dropped_count(self, dropped_count):
        """
        Sets the dropped_count of this DropRequestDTO.
        The number of flow files that have been dropped thus far.

        :param dropped_count: The dropped_count of this DropRequestDTO.
        :type: int
        """

        self._dropped_count = dropped_count

    @property
    def dropped_size(self):
        """
        Gets the dropped_size of this DropRequestDTO.
        The size of flow files that have been dropped thus far in bytes.

        :return: The dropped_size of this DropRequestDTO.
        :rtype: int
        """
        return self._dropped_size

    @dropped_size.setter
    def dropped_size(self, dropped_size):
        """
        Sets the dropped_size of this DropRequestDTO.
        The size of flow files that have been dropped thus far in bytes.

        :param dropped_size: The dropped_size of this DropRequestDTO.
        :type: int
        """

        self._dropped_size = dropped_size

    @property
    def dropped(self):
        """
        Gets the dropped of this DropRequestDTO.
        The count and size of flow files that have been dropped thus far.

        :return: The dropped of this DropRequestDTO.
        :rtype: str
        """
        return self._dropped

    @dropped.setter
    def dropped(self, dropped):
        """
        Sets the dropped of this DropRequestDTO.
        The count and size of flow files that have been dropped thus far.

        :param dropped: The dropped of this DropRequestDTO.
        :type: str
        """

        self._dropped = dropped

    @property
    def state(self):
        """
        Gets the state of this DropRequestDTO.
        The current state of the drop request.

        :return: The state of this DropRequestDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DropRequestDTO.
        The current state of the drop request.

        :param state: The state of this DropRequestDTO.
        :type: str
        """

        self._state = state

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
        if not isinstance(other, DropRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
