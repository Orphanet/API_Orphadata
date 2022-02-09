# coding: utf-8

from __future__ import absolute_import

from api.models.base_model_ import Model
from api.models.product4_disorder import Product4Disorder  # noqa: F401,E501
from api import util


class Product4(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, disorder: Product4Disorder=None, source: str=None, validation_status: str=None, online: str=None, validation_date: str=None):  # noqa: E501
        """Product4 - a model defined in Swagger

        :param disorder: The disorder of this Product4.  # noqa: E501
        :type disorder: Product4Disorder
        :param source: The source of this Product4.  # noqa: E501
        :type source: str
        :param validation_status: The validation_status of this Product4.  # noqa: E501
        :type validation_status: str
        :param online: The online of this Product4.  # noqa: E501
        :type online: str
        :param validation_date: The validation_date of this Product4.  # noqa: E501
        :type validation_date: str
        """
        self.swagger_types = {
            'disorder': Product4Disorder,
            'source': str,
            'validation_status': str,
            'online': str,
            'validation_date': str
        }

        self.attribute_map = {
            'disorder': 'Disorder',
            'source': 'Source',
            'validation_status': 'ValidationStatus',
            'online': 'Online',
            'validation_date': 'ValidationDate'
        }
        self._disorder = disorder
        self._source = source
        self._validation_status = validation_status
        self._online = online
        self._validation_date = validation_date

    @classmethod
    def from_dict(cls, dikt) -> 'Product4':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product4 of this Product4.  # noqa: E501
        :rtype: Product4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def disorder(self) -> Product4Disorder:
        """Gets the disorder of this Product4.


        :return: The disorder of this Product4.
        :rtype: Product4Disorder
        """
        return self._disorder

    @disorder.setter
    def disorder(self, disorder: Product4Disorder):
        """Sets the disorder of this Product4.


        :param disorder: The disorder of this Product4.
        :type disorder: Product4Disorder
        """

        self._disorder = disorder

    @property
    def source(self) -> str:
        """Gets the source of this Product4.


        :return: The source of this Product4.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this Product4.


        :param source: The source of this Product4.
        :type source: str
        """

        self._source = source

    @property
    def validation_status(self) -> str:
        """Gets the validation_status of this Product4.


        :return: The validation_status of this Product4.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status: str):
        """Sets the validation_status of this Product4.


        :param validation_status: The validation_status of this Product4.
        :type validation_status: str
        """

        self._validation_status = validation_status

    @property
    def online(self) -> str:
        """Gets the online of this Product4.


        :return: The online of this Product4.
        :rtype: str
        """
        return self._online

    @online.setter
    def online(self, online: str):
        """Sets the online of this Product4.


        :param online: The online of this Product4.
        :type online: str
        """

        self._online = online

    @property
    def validation_date(self) -> str:
        """Gets the validation_date of this Product4.


        :return: The validation_date of this Product4.
        :rtype: str
        """
        return self._validation_date

    @validation_date.setter
    def validation_date(self, validation_date: str):
        """Sets the validation_date of this Product4.


        :param validation_date: The validation_date of this Product4.
        :type validation_date: str
        """

        self._validation_date = validation_date