# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product1 import Product1  # noqa: F401,E501
from swagger_server import util


class Product1List(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """Product1List - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Product1List':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product1_list of this Product1List.  # noqa: E501
        :rtype: Product1List
        """
        return util.deserialize_model(dikt, cls)
