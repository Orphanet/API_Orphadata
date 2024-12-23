# coding: utf-8

from __future__ import absolute_import

from api.models.base_model_ import Model
from api.models.product1_disorder_mapping_relation import Product1DisorderMappingRelation  # noqa: F401,E501
from api.models.product1_disorder_mapping_validation_status import Product1DisorderMappingValidationStatus  # noqa: F401,E501
from api import util


class Product1ExternalReference(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, source: str=None, reference: str=None, disorder_mapping_relation: Product1DisorderMappingRelation=None, disorder_mapping_icd_relation: str=None, disorder_mapping_validation_status: Product1DisorderMappingValidationStatus=None):  # noqa: E501
        """Product1ExternalReference - a model defined in Swagger

        :param source: The source of this Product1ExternalReference.  # noqa: E501
        :type source: str
        :param reference: The reference of this Product1ExternalReference.  # noqa: E501
        :type reference: str
        :param disorder_mapping_relation: The disorder_mapping_relation of this Product1ExternalReference.  # noqa: E501
        :type disorder_mapping_relation: Product1DisorderMappingRelation
        :param disorder_mapping_icd_relation: The disorder_mapping_icd_relation of this Product1ExternalReference.  # noqa: E501
        :type disorder_mapping_icd_relation: str
        :param disorder_mapping_validation_status: The disorder_mapping_validation_status of this Product1ExternalReference.  # noqa: E501
        :type disorder_mapping_validation_status: Product1DisorderMappingValidationStatus
        """
        self.swagger_types = {
            'source': str,
            'reference': str,
            'disorder_mapping_relation': Product1DisorderMappingRelation,
            'disorder_mapping_icd_relation': str,
            'disorder_mapping_validation_status': Product1DisorderMappingValidationStatus
        }

        self.attribute_map = {
            'source': 'Source',
            'reference': 'Reference',
            'disorder_mapping_relation': 'DisorderMappingRelation',
            'disorder_mapping_icd_relation': 'DisorderMappingICDRelation',
            'disorder_mapping_validation_status': 'DisorderMappingValidationStatus'
        }
        self._source = source
        self._reference = reference
        self._disorder_mapping_relation = disorder_mapping_relation
        self._disorder_mapping_icd_relation = disorder_mapping_icd_relation
        self._disorder_mapping_validation_status = disorder_mapping_validation_status

    @classmethod
    def from_dict(cls, dikt) -> 'Product1ExternalReference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product1_ExternalReference of this Product1ExternalReference.  # noqa: E501
        :rtype: Product1ExternalReference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self) -> str:
        """Gets the source of this Product1ExternalReference.


        :return: The source of this Product1ExternalReference.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this Product1ExternalReference.


        :param source: The source of this Product1ExternalReference.
        :type source: str
        """

        self._source = source

    @property
    def reference(self) -> str:
        """Gets the reference of this Product1ExternalReference.


        :return: The reference of this Product1ExternalReference.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Product1ExternalReference.


        :param reference: The reference of this Product1ExternalReference.
        :type reference: str
        """

        self._reference = reference

    @property
    def disorder_mapping_relation(self) -> Product1DisorderMappingRelation:
        """Gets the disorder_mapping_relation of this Product1ExternalReference.


        :return: The disorder_mapping_relation of this Product1ExternalReference.
        :rtype: Product1DisorderMappingRelation
        """
        return self._disorder_mapping_relation

    @disorder_mapping_relation.setter
    def disorder_mapping_relation(self, disorder_mapping_relation: Product1DisorderMappingRelation):
        """Sets the disorder_mapping_relation of this Product1ExternalReference.


        :param disorder_mapping_relation: The disorder_mapping_relation of this Product1ExternalReference.
        :type disorder_mapping_relation: Product1DisorderMappingRelation
        """

        self._disorder_mapping_relation = disorder_mapping_relation

    @property
    def disorder_mapping_icd_relation(self) -> str:
        """Gets the disorder_mapping_icd_relation of this Product1ExternalReference.


        :return: The disorder_mapping_icd_relation of this Product1ExternalReference.
        :rtype: str
        """
        return self._disorder_mapping_icd_relation

    @disorder_mapping_icd_relation.setter
    def disorder_mapping_icd_relation(self, disorder_mapping_icd_relation: str):
        """Sets the disorder_mapping_icd_relation of this Product1ExternalReference.


        :param disorder_mapping_icd_relation: The disorder_mapping_icd_relation of this Product1ExternalReference.
        :type disorder_mapping_icd_relation: str
        """

        self._disorder_mapping_icd_relation = disorder_mapping_icd_relation

    @property
    def disorder_mapping_validation_status(self) -> Product1DisorderMappingValidationStatus:
        """Gets the disorder_mapping_validation_status of this Product1ExternalReference.


        :return: The disorder_mapping_validation_status of this Product1ExternalReference.
        :rtype: Product1DisorderMappingValidationStatus
        """
        return self._disorder_mapping_validation_status

    @disorder_mapping_validation_status.setter
    def disorder_mapping_validation_status(self, disorder_mapping_validation_status: Product1DisorderMappingValidationStatus):
        """Sets the disorder_mapping_validation_status of this Product1ExternalReference.


        :param disorder_mapping_validation_status: The disorder_mapping_validation_status of this Product1ExternalReference.
        :type disorder_mapping_validation_status: Product1DisorderMappingValidationStatus
        """

        self._disorder_mapping_validation_status = disorder_mapping_validation_status
