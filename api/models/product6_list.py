# coding: utf-8

from __future__ import absolute_import

from api.models.base_model_ import Model
from api import util


class Product6List(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """Product6List - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Product6List':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product6_list of this Product6List.  # noqa: E501
        :rtype: Product6List
        """
        return util.deserialize_model(dikt, cls)
