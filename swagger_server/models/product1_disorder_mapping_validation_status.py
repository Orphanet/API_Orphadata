# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Product1DisorderMappingValidationStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, orph_acode: int=None, name: str=None):  # noqa: E501
        """Product1DisorderMappingValidationStatus - a model defined in Swagger

        :param orph_acode: The orph_acode of this Product1DisorderMappingValidationStatus.  # noqa: E501
        :type orph_acode: int
        :param name: The name of this Product1DisorderMappingValidationStatus.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'orph_acode': int,
            'name': str
        }

        self.attribute_map = {
            'orph_acode': 'ORPHAcode',
            'name': 'Name'
        }
        self._orph_acode = orph_acode
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Product1DisorderMappingValidationStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product1_DisorderMappingValidationStatus of this Product1DisorderMappingValidationStatus.  # noqa: E501
        :rtype: Product1DisorderMappingValidationStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orph_acode(self) -> int:
        """Gets the orph_acode of this Product1DisorderMappingValidationStatus.


        :return: The orph_acode of this Product1DisorderMappingValidationStatus.
        :rtype: int
        """
        return self._orph_acode

    @orph_acode.setter
    def orph_acode(self, orph_acode: int):
        """Sets the orph_acode of this Product1DisorderMappingValidationStatus.


        :param orph_acode: The orph_acode of this Product1DisorderMappingValidationStatus.
        :type orph_acode: int
        """

        self._orph_acode = orph_acode

    @property
    def name(self) -> str:
        """Gets the name of this Product1DisorderMappingValidationStatus.


        :return: The name of this Product1DisorderMappingValidationStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product1DisorderMappingValidationStatus.


        :param name: The name of this Product1DisorderMappingValidationStatus.
        :type name: str
        """

        self._name = name