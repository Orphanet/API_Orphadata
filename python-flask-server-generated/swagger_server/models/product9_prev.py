# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product9_prev_prevalence import Product9PrevPrevalence  # noqa: F401,E501
from swagger_server import util


class Product9Prev(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, orph_acode: str=None, expert_link: str=None, name: str=None, disorder_type: str=None, disorder_group: str=None, prevalence: List[Product9PrevPrevalence]=None):  # noqa: E501
        """Product9Prev - a model defined in Swagger

        :param orph_acode: The orph_acode of this Product9Prev.  # noqa: E501
        :type orph_acode: str
        :param expert_link: The expert_link of this Product9Prev.  # noqa: E501
        :type expert_link: str
        :param name: The name of this Product9Prev.  # noqa: E501
        :type name: str
        :param disorder_type: The disorder_type of this Product9Prev.  # noqa: E501
        :type disorder_type: str
        :param disorder_group: The disorder_group of this Product9Prev.  # noqa: E501
        :type disorder_group: str
        :param prevalence: The prevalence of this Product9Prev.  # noqa: E501
        :type prevalence: List[Product9PrevPrevalence]
        """
        self.swagger_types = {
            'orph_acode': str,
            'expert_link': str,
            'name': str,
            'disorder_type': str,
            'disorder_group': str,
            'prevalence': List[Product9PrevPrevalence]
        }

        self.attribute_map = {
            'orph_acode': 'ORPHAcode',
            'expert_link': 'ExpertLink',
            'name': 'Name',
            'disorder_type': 'DisorderType',
            'disorder_group': 'DisorderGroup',
            'prevalence': 'Prevalence'
        }
        self._orph_acode = orph_acode
        self._expert_link = expert_link
        self._name = name
        self._disorder_type = disorder_type
        self._disorder_group = disorder_group
        self._prevalence = prevalence

    @classmethod
    def from_dict(cls, dikt) -> 'Product9Prev':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product9_prev of this Product9Prev.  # noqa: E501
        :rtype: Product9Prev
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orph_acode(self) -> str:
        """Gets the orph_acode of this Product9Prev.


        :return: The orph_acode of this Product9Prev.
        :rtype: str
        """
        return self._orph_acode

    @orph_acode.setter
    def orph_acode(self, orph_acode: str):
        """Sets the orph_acode of this Product9Prev.


        :param orph_acode: The orph_acode of this Product9Prev.
        :type orph_acode: str
        """
        if orph_acode is None:
            raise ValueError("Invalid value for `orph_acode`, must not be `None`")  # noqa: E501

        self._orph_acode = orph_acode

    @property
    def expert_link(self) -> str:
        """Gets the expert_link of this Product9Prev.


        :return: The expert_link of this Product9Prev.
        :rtype: str
        """
        return self._expert_link

    @expert_link.setter
    def expert_link(self, expert_link: str):
        """Sets the expert_link of this Product9Prev.


        :param expert_link: The expert_link of this Product9Prev.
        :type expert_link: str
        """

        self._expert_link = expert_link

    @property
    def name(self) -> str:
        """Gets the name of this Product9Prev.


        :return: The name of this Product9Prev.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product9Prev.


        :param name: The name of this Product9Prev.
        :type name: str
        """

        self._name = name

    @property
    def disorder_type(self) -> str:
        """Gets the disorder_type of this Product9Prev.


        :return: The disorder_type of this Product9Prev.
        :rtype: str
        """
        return self._disorder_type

    @disorder_type.setter
    def disorder_type(self, disorder_type: str):
        """Sets the disorder_type of this Product9Prev.


        :param disorder_type: The disorder_type of this Product9Prev.
        :type disorder_type: str
        """

        self._disorder_type = disorder_type

    @property
    def disorder_group(self) -> str:
        """Gets the disorder_group of this Product9Prev.


        :return: The disorder_group of this Product9Prev.
        :rtype: str
        """
        return self._disorder_group

    @disorder_group.setter
    def disorder_group(self, disorder_group: str):
        """Sets the disorder_group of this Product9Prev.


        :param disorder_group: The disorder_group of this Product9Prev.
        :type disorder_group: str
        """

        self._disorder_group = disorder_group

    @property
    def prevalence(self) -> List[Product9PrevPrevalence]:
        """Gets the prevalence of this Product9Prev.


        :return: The prevalence of this Product9Prev.
        :rtype: List[Product9PrevPrevalence]
        """
        return self._prevalence

    @prevalence.setter
    def prevalence(self, prevalence: List[Product9PrevPrevalence]):
        """Sets the prevalence of this Product9Prev.


        :param prevalence: The prevalence of this Product9Prev.
        :type prevalence: List[Product9PrevPrevalence]
        """

        self._prevalence = prevalence
