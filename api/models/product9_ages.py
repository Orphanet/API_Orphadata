# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from api.models.base_model_ import Model
from api import util


class Product9Ages(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, orph_acode: int=None, expert_link: str=None, name: str=None, disorder_type: str=None, disorder_group: str=None, average_age_of_onset: List[str]=None, average_age_of_death: List[str]=None, type_of_inheritance: List[str]=None):  # noqa: E501
        """Product9Ages - a model defined in Swagger

        :param orph_acode: The orph_acode of this Product9Ages.  # noqa: E501
        :type orph_acode: int
        :param expert_link: The expert_link of this Product9Ages.  # noqa: E501
        :type expert_link: str
        :param name: The name of this Product9Ages.  # noqa: E501
        :type name: str
        :param disorder_type: The disorder_type of this Product9Ages.  # noqa: E501
        :type disorder_type: str
        :param disorder_group: The disorder_group of this Product9Ages.  # noqa: E501
        :type disorder_group: str
        :param average_age_of_onset: The average_age_of_onset of this Product9Ages.  # noqa: E501
        :type average_age_of_onset: List[str]
        :param average_age_of_death: The average_age_of_death of this Product9Ages.  # noqa: E501
        :type average_age_of_death: List[str]
        :param type_of_inheritance: The type_of_inheritance of this Product9Ages.  # noqa: E501
        :type type_of_inheritance: List[str]
        """
        self.swagger_types = {
            'orph_acode': int,
            'expert_link': str,
            'name': str,
            'disorder_type': str,
            'disorder_group': str,
            'average_age_of_onset': List[str],
            'average_age_of_death': List[str],
            'type_of_inheritance': List[str]
        }

        self.attribute_map = {
            'orph_acode': 'ORPHAcode',
            'expert_link': 'ExpertLink',
            'name': 'Name',
            'disorder_type': 'DisorderType',
            'disorder_group': 'DisorderGroup',
            'average_age_of_onset': 'AverageAgeOfOnset',
            'average_age_of_death': 'AverageAgeOfDeath',
            'type_of_inheritance': 'TypeOfInheritance'
        }
        self._orph_acode = orph_acode
        self._expert_link = expert_link
        self._name = name
        self._disorder_type = disorder_type
        self._disorder_group = disorder_group
        self._average_age_of_onset = average_age_of_onset
        self._average_age_of_death = average_age_of_death
        self._type_of_inheritance = type_of_inheritance

    @classmethod
    def from_dict(cls, dikt) -> 'Product9Ages':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product9_ages of this Product9Ages.  # noqa: E501
        :rtype: Product9Ages
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orph_acode(self) -> int:
        """Gets the orph_acode of this Product9Ages.


        :return: The orph_acode of this Product9Ages.
        :rtype: int
        """
        return self._orph_acode

    @orph_acode.setter
    def orph_acode(self, orph_acode: int):
        """Sets the orph_acode of this Product9Ages.


        :param orph_acode: The orph_acode of this Product9Ages.
        :type orph_acode: int
        """
        if orph_acode is None:
            raise ValueError("Invalid value for `orph_acode`, must not be `None`")  # noqa: E501

        self._orph_acode = orph_acode

    @property
    def expert_link(self) -> str:
        """Gets the expert_link of this Product9Ages.


        :return: The expert_link of this Product9Ages.
        :rtype: str
        """
        return self._expert_link

    @expert_link.setter
    def expert_link(self, expert_link: str):
        """Sets the expert_link of this Product9Ages.


        :param expert_link: The expert_link of this Product9Ages.
        :type expert_link: str
        """

        self._expert_link = expert_link

    @property
    def name(self) -> str:
        """Gets the name of this Product9Ages.


        :return: The name of this Product9Ages.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product9Ages.


        :param name: The name of this Product9Ages.
        :type name: str
        """

        self._name = name

    @property
    def disorder_type(self) -> str:
        """Gets the disorder_type of this Product9Ages.


        :return: The disorder_type of this Product9Ages.
        :rtype: str
        """
        return self._disorder_type

    @disorder_type.setter
    def disorder_type(self, disorder_type: str):
        """Sets the disorder_type of this Product9Ages.


        :param disorder_type: The disorder_type of this Product9Ages.
        :type disorder_type: str
        """

        self._disorder_type = disorder_type

    @property
    def disorder_group(self) -> str:
        """Gets the disorder_group of this Product9Ages.


        :return: The disorder_group of this Product9Ages.
        :rtype: str
        """
        return self._disorder_group

    @disorder_group.setter
    def disorder_group(self, disorder_group: str):
        """Sets the disorder_group of this Product9Ages.


        :param disorder_group: The disorder_group of this Product9Ages.
        :type disorder_group: str
        """

        self._disorder_group = disorder_group

    @property
    def average_age_of_onset(self) -> List[str]:
        """Gets the average_age_of_onset of this Product9Ages.


        :return: The average_age_of_onset of this Product9Ages.
        :rtype: List[str]
        """
        return self._average_age_of_onset

    @average_age_of_onset.setter
    def average_age_of_onset(self, average_age_of_onset: List[str]):
        """Sets the average_age_of_onset of this Product9Ages.


        :param average_age_of_onset: The average_age_of_onset of this Product9Ages.
        :type average_age_of_onset: List[str]
        """

        self._average_age_of_onset = average_age_of_onset

    @property
    def average_age_of_death(self) -> List[str]:
        """Gets the average_age_of_death of this Product9Ages.


        :return: The average_age_of_death of this Product9Ages.
        :rtype: List[str]
        """
        return self._average_age_of_death

    @average_age_of_death.setter
    def average_age_of_death(self, average_age_of_death: List[str]):
        """Sets the average_age_of_death of this Product9Ages.


        :param average_age_of_death: The average_age_of_death of this Product9Ages.
        :type average_age_of_death: List[str]
        """

        self._average_age_of_death = average_age_of_death

    @property
    def type_of_inheritance(self) -> List[str]:
        """Gets the type_of_inheritance of this Product9Ages.


        :return: The type_of_inheritance of this Product9Ages.
        :rtype: List[str]
        """
        return self._type_of_inheritance

    @type_of_inheritance.setter
    def type_of_inheritance(self, type_of_inheritance: List[str]):
        """Sets the type_of_inheritance of this Product9Ages.


        :param type_of_inheritance: The type_of_inheritance of this Product9Ages.
        :type type_of_inheritance: List[str]
        """

        self._type_of_inheritance = type_of_inheritance
