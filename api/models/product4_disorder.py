# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from api.models.base_model_ import Model
from api.models.product4_disorder_hpo_disorder_association import Product4DisorderHPODisorderAssociation  # noqa: F401,E501
from api import util


class Product4Disorder(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, orph_acode: int=None, expert_link: str=None, name: str=None, disorder_type: str=None, disorder_group: str=None, hpo_disorder_association: List[Product4DisorderHPODisorderAssociation]=None):  # noqa: E501
        """Product4Disorder - a model defined in Swagger

        :param orph_acode: The orph_acode of this Product4Disorder.  # noqa: E501
        :type orph_acode: int
        :param expert_link: The expert_link of this Product4Disorder.  # noqa: E501
        :type expert_link: str
        :param name: The name of this Product4Disorder.  # noqa: E501
        :type name: str
        :param disorder_type: The disorder_type of this Product4Disorder.  # noqa: E501
        :type disorder_type: str
        :param disorder_group: The disorder_group of this Product4Disorder.  # noqa: E501
        :type disorder_group: str
        :param hpo_disorder_association: The hpo_disorder_association of this Product4Disorder.  # noqa: E501
        :type hpo_disorder_association: List[Product4DisorderHPODisorderAssociation]
        """
        self.swagger_types = {
            'orph_acode': int,
            'expert_link': str,
            'name': str,
            'disorder_type': str,
            'disorder_group': str,
            'hpo_disorder_association': List[Product4DisorderHPODisorderAssociation]
        }

        self.attribute_map = {
            'orph_acode': 'ORPHAcode',
            'expert_link': 'ExpertLink',
            'name': 'Name',
            'disorder_type': 'DisorderType',
            'disorder_group': 'DisorderGroup',
            'hpo_disorder_association': 'HPODisorderAssociation'
        }
        self._orph_acode = orph_acode
        self._expert_link = expert_link
        self._name = name
        self._disorder_type = disorder_type
        self._disorder_group = disorder_group
        self._hpo_disorder_association = hpo_disorder_association

    @classmethod
    def from_dict(cls, dikt) -> 'Product4Disorder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product4_Disorder of this Product4Disorder.  # noqa: E501
        :rtype: Product4Disorder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orph_acode(self) -> int:
        """Gets the orph_acode of this Product4Disorder.


        :return: The orph_acode of this Product4Disorder.
        :rtype: int
        """
        return self._orph_acode

    @orph_acode.setter
    def orph_acode(self, orph_acode: int):
        """Sets the orph_acode of this Product4Disorder.


        :param orph_acode: The orph_acode of this Product4Disorder.
        :type orph_acode: int
        """

        self._orph_acode = orph_acode

    @property
    def expert_link(self) -> str:
        """Gets the expert_link of this Product4Disorder.


        :return: The expert_link of this Product4Disorder.
        :rtype: str
        """
        return self._expert_link

    @expert_link.setter
    def expert_link(self, expert_link: str):
        """Sets the expert_link of this Product4Disorder.


        :param expert_link: The expert_link of this Product4Disorder.
        :type expert_link: str
        """

        self._expert_link = expert_link

    @property
    def name(self) -> str:
        """Gets the name of this Product4Disorder.


        :return: The name of this Product4Disorder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product4Disorder.


        :param name: The name of this Product4Disorder.
        :type name: str
        """

        self._name = name

    @property
    def disorder_type(self) -> str:
        """Gets the disorder_type of this Product4Disorder.


        :return: The disorder_type of this Product4Disorder.
        :rtype: str
        """
        return self._disorder_type

    @disorder_type.setter
    def disorder_type(self, disorder_type: str):
        """Sets the disorder_type of this Product4Disorder.


        :param disorder_type: The disorder_type of this Product4Disorder.
        :type disorder_type: str
        """

        self._disorder_type = disorder_type

    @property
    def disorder_group(self) -> str:
        """Gets the disorder_group of this Product4Disorder.


        :return: The disorder_group of this Product4Disorder.
        :rtype: str
        """
        return self._disorder_group

    @disorder_group.setter
    def disorder_group(self, disorder_group: str):
        """Sets the disorder_group of this Product4Disorder.


        :param disorder_group: The disorder_group of this Product4Disorder.
        :type disorder_group: str
        """

        self._disorder_group = disorder_group

    @property
    def hpo_disorder_association(self) -> List[Product4DisorderHPODisorderAssociation]:
        """Gets the hpo_disorder_association of this Product4Disorder.


        :return: The hpo_disorder_association of this Product4Disorder.
        :rtype: List[Product4DisorderHPODisorderAssociation]
        """
        return self._hpo_disorder_association

    @hpo_disorder_association.setter
    def hpo_disorder_association(self, hpo_disorder_association: List[Product4DisorderHPODisorderAssociation]):
        """Sets the hpo_disorder_association of this Product4Disorder.


        :param hpo_disorder_association: The hpo_disorder_association of this Product4Disorder.
        :type hpo_disorder_association: List[Product4DisorderHPODisorderAssociation]
        """

        self._hpo_disorder_association = hpo_disorder_association
