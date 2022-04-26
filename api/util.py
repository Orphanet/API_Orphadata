import datetime
import six
import typing



from connexion.apps.flask_app import FlaskJSONEncoder

from api.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.swagger_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return FlaskJSONEncoder.default(self, o)



def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.swagger_types:
        return data

    for attr, attr_type in six.iteritems(instance.swagger_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}


def build_query_elements(args: typing.Dict):
    ALLOWED_QUERY_FIELDS = {
        "disorder-name": {
            "query_type": "query_string",
            "field": "Preferred term",
            "value": None
        },
        "disorder-synonym": {
            "query_type": "query_string",
            "field": "Synonym",
            "value": None
        },
        "disorder-definition": {
            "query_type": "query_string",
            "field": "SummaryInformation.Definition",
            "value": None
        },
        "reference-code": {
            "query_type": "nested_query_string",
            "field": "ExternalReference.Reference",
            "value": None
        },
        "reference-db": {
            "query_type": "nested_match",
            "field": "ExternalReference.Source",
            "value": None
        },
        "mapping-level": {
            "query_type": "nested_query_string",
            "field": "ExternalReference.DisorderMappingRelation",
            "value": None
        }
    }

    query_elements = []
    nested_elements = []

    for key, value in args.items():
        if key in ALLOWED_QUERY_FIELDS:
            element = ALLOWED_QUERY_FIELDS[key]

            if element["query_type"] == "query_string":
                query_elements.append(
                    {
                        "query_string": {
                            "default_field": element["field"], 
                            "query": value,
                            "default_operator": "AND"
                        }
                    }
                )
            elif "nested" in element["query_type"]:
                if "match" in element["query_type"]:
                    nested_elements.append(
                        {
                            "match": {
                                element["field"]: value
                            }
                        }
                    )
                elif "query_string" in element["query_type"]:
                    nested_elements.append(
                        {
                            "query_string": {
                                "default_field": element["field"],
                                "query": value,
                                "default_operator": "AND"
                            }
                        }
                    )

    if nested_elements:
        query_elements.append(
            {
                "nested": {
                    "path": "ExternalReference",  
                    "query": {
                        "bool": {
                            "must": nested_elements
                        }
                    }
                }
            }
        )

    return query_elements




