# coding: utf-8

from __future__ import absolute_import

from api.models.base_model_ import Model
from api import util


class ListHchid(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """ListHchid - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ListHchid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The list_hchid of this ListHchid.  # noqa: E501
        :rtype: ListHchid
        """
        return util.deserialize_model(dikt, cls)
