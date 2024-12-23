# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from api.models.base_model_ import Model
from api.models.product6_disorder_gene_association import Product6DisorderGeneAssociation  # noqa: F401,E501
from api import util


class Product6(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, orph_acode: int=None, expert_link: str=None, name: str=None, disorder_type: str=None, disorder_group: str=None, disorder_gene_association: List[Product6DisorderGeneAssociation]=None):  # noqa: E501
        """Product6 - a model defined in Swagger

        :param orph_acode: The orph_acode of this Product6.  # noqa: E501
        :type orph_acode: int
        :param expert_link: The expert_link of this Product6.  # noqa: E501
        :type expert_link: str
        :param name: The name of this Product6.  # noqa: E501
        :type name: str
        :param disorder_type: The disorder_type of this Product6.  # noqa: E501
        :type disorder_type: str
        :param disorder_group: The disorder_group of this Product6.  # noqa: E501
        :type disorder_group: str
        :param disorder_gene_association: The disorder_gene_association of this Product6.  # noqa: E501
        :type disorder_gene_association: List[Product6DisorderGeneAssociation]
        """
        self.swagger_types = {
            'orph_acode': int,
            'expert_link': str,
            'name': str,
            'disorder_type': str,
            'disorder_group': str,
            'disorder_gene_association': List[Product6DisorderGeneAssociation]
        }

        self.attribute_map = {
            'orph_acode': 'ORPHAcode',
            'expert_link': 'ExpertLink',
            'name': 'Name',
            'disorder_type': 'DisorderType',
            'disorder_group': 'DisorderGroup',
            'disorder_gene_association': 'DisorderGeneAssociation'
        }
        self._orph_acode = orph_acode
        self._expert_link = expert_link
        self._name = name
        self._disorder_type = disorder_type
        self._disorder_group = disorder_group
        self._disorder_gene_association = disorder_gene_association

    @classmethod
    def from_dict(cls, dikt) -> 'Product6':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product6 of this Product6.  # noqa: E501
        :rtype: Product6
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orph_acode(self) -> int:
        """Gets the orph_acode of this Product6.


        :return: The orph_acode of this Product6.
        :rtype: int
        """
        return self._orph_acode

    @orph_acode.setter
    def orph_acode(self, orph_acode: int):
        """Sets the orph_acode of this Product6.


        :param orph_acode: The orph_acode of this Product6.
        :type orph_acode: int
        """
        if orph_acode is None:
            raise ValueError("Invalid value for `orph_acode`, must not be `None`")  # noqa: E501

        self._orph_acode = orph_acode

    @property
    def expert_link(self) -> str:
        """Gets the expert_link of this Product6.


        :return: The expert_link of this Product6.
        :rtype: str
        """
        return self._expert_link

    @expert_link.setter
    def expert_link(self, expert_link: str):
        """Sets the expert_link of this Product6.


        :param expert_link: The expert_link of this Product6.
        :type expert_link: str
        """

        self._expert_link = expert_link

    @property
    def name(self) -> str:
        """Gets the name of this Product6.


        :return: The name of this Product6.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product6.


        :param name: The name of this Product6.
        :type name: str
        """

        self._name = name

    @property
    def disorder_type(self) -> str:
        """Gets the disorder_type of this Product6.


        :return: The disorder_type of this Product6.
        :rtype: str
        """
        return self._disorder_type

    @disorder_type.setter
    def disorder_type(self, disorder_type: str):
        """Sets the disorder_type of this Product6.


        :param disorder_type: The disorder_type of this Product6.
        :type disorder_type: str
        """

        self._disorder_type = disorder_type

    @property
    def disorder_group(self) -> str:
        """Gets the disorder_group of this Product6.


        :return: The disorder_group of this Product6.
        :rtype: str
        """
        return self._disorder_group

    @disorder_group.setter
    def disorder_group(self, disorder_group: str):
        """Sets the disorder_group of this Product6.


        :param disorder_group: The disorder_group of this Product6.
        :type disorder_group: str
        """

        self._disorder_group = disorder_group

    @property
    def disorder_gene_association(self) -> List[Product6DisorderGeneAssociation]:
        """Gets the disorder_gene_association of this Product6.


        :return: The disorder_gene_association of this Product6.
        :rtype: List[Product6DisorderGeneAssociation]
        """
        return self._disorder_gene_association

    @disorder_gene_association.setter
    def disorder_gene_association(self, disorder_gene_association: List[Product6DisorderGeneAssociation]):
        """Sets the disorder_gene_association of this Product6.


        :param disorder_gene_association: The disorder_gene_association of this Product6.
        :type disorder_gene_association: List[Product6DisorderGeneAssociation]
        """

        self._disorder_gene_association = disorder_gene_association
