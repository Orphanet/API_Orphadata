# coding: utf-8

from __future__ import absolute_import

from api.models.base_model_ import Model
from api import util


class Product6GeneDisorder(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, orph_acode: int=None, expert_link: str=None, name: str=None, disorder_type: str=None, disorder_group: str=None):  # noqa: E501
        """Product6GeneDisorder - a model defined in Swagger

        :param orph_acode: The orph_acode of this Product6GeneDisorder.  # noqa: E501
        :type orph_acode: int
        :param expert_link: The expert_link of this Product6GeneDisorder.  # noqa: E501
        :type expert_link: str
        :param name: The name of this Product6GeneDisorder.  # noqa: E501
        :type name: str
        :param disorder_type: The disorder_type of this Product6GeneDisorder.  # noqa: E501
        :type disorder_type: str
        :param disorder_group: The disorder_group of this Product6GeneDisorder.  # noqa: E501
        :type disorder_group: str
        """
        self.swagger_types = {
            'orph_acode': int,
            'expert_link': str,
            'name': str,
            'disorder_type': str,
            'disorder_group': str
        }

        self.attribute_map = {
            'orph_acode': 'ORPHAcode',
            'expert_link': 'ExpertLink',
            'name': 'Name',
            'disorder_type': 'DisorderType',
            'disorder_group': 'DisorderGroup'
        }
        self._orph_acode = orph_acode
        self._expert_link = expert_link
        self._name = name
        self._disorder_type = disorder_type
        self._disorder_group = disorder_group

    @classmethod
    def from_dict(cls, dikt) -> 'Product6GeneDisorder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product6_gene_disorder of this Product6GeneDisorder.  # noqa: E501
        :rtype: Product6GeneDisorder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orph_acode(self) -> int:
        """Gets the orph_acode of this Product6GeneDisorder.


        :return: The orph_acode of this Product6GeneDisorder.
        :rtype: int
        """
        return self._orph_acode

    @orph_acode.setter
    def orph_acode(self, orph_acode: int):
        """Sets the orph_acode of this Product6GeneDisorder.


        :param orph_acode: The orph_acode of this Product6GeneDisorder.
        :type orph_acode: int
        """

        self._orph_acode = orph_acode

    @property
    def expert_link(self) -> str:
        """Gets the expert_link of this Product6GeneDisorder.


        :return: The expert_link of this Product6GeneDisorder.
        :rtype: str
        """
        return self._expert_link

    @expert_link.setter
    def expert_link(self, expert_link: str):
        """Sets the expert_link of this Product6GeneDisorder.


        :param expert_link: The expert_link of this Product6GeneDisorder.
        :type expert_link: str
        """

        self._expert_link = expert_link

    @property
    def name(self) -> str:
        """Gets the name of this Product6GeneDisorder.


        :return: The name of this Product6GeneDisorder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product6GeneDisorder.


        :param name: The name of this Product6GeneDisorder.
        :type name: str
        """

        self._name = name

    @property
    def disorder_type(self) -> str:
        """Gets the disorder_type of this Product6GeneDisorder.


        :return: The disorder_type of this Product6GeneDisorder.
        :rtype: str
        """
        return self._disorder_type

    @disorder_type.setter
    def disorder_type(self, disorder_type: str):
        """Sets the disorder_type of this Product6GeneDisorder.


        :param disorder_type: The disorder_type of this Product6GeneDisorder.
        :type disorder_type: str
        """

        self._disorder_type = disorder_type

    @property
    def disorder_group(self) -> str:
        """Gets the disorder_group of this Product6GeneDisorder.


        :return: The disorder_group of this Product6GeneDisorder.
        :rtype: str
        """
        return self._disorder_group

    @disorder_group.setter
    def disorder_group(self, disorder_group: str):
        """Sets the disorder_group of this Product6GeneDisorder.


        :param disorder_group: The disorder_group of this Product6GeneDisorder.
        :type disorder_group: str
        """

        self._disorder_group = disorder_group
