import config
import controllers.query_controller as qc


def medical_specialty_parent_by_orphacode(orphacode):  # noqa: E501
    """Get associated genes and genes information of a clinical entity searching by its ORPHAcode.

    The result is a set of data includes ORPhacode, preferred term, expertlink, group and type of the selected clinical entity, relationship between genes and the searched disease and symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product6
    """
    es = config.elastic_server
    index = "en_product7"

    query = {
        "query": {
            "term": {
                "ORPHAcode": int(orphacode)
            }
        },
        # "_source": ["ORPHAcode"]
    }

    response = qc.single_res(es, index, query)
    return response


def medical_specialty_parents():
    es = config.elastic_server
    index = "en_product7"

    query = {
        "query": {
            "match_all": {}
        },
        "_source": ["DisorderDisorderAssociation.TargetDisorder"]
    }

    response = qc.multiple_res(es, index, query, size=config.scroll_size)

    response_parsed = []
    for hit in response:
        parent = {
            "ORPHAcode": hit["DisorderDisorderAssociation"][0]["TargetDisorder"]["ORPHAcode"],
            "Preferred term": hit["DisorderDisorderAssociation"][0]["TargetDisorder"]["Preferred term"]
            }
        if parent not in response_parsed:
            response_parsed.append(parent)

    return sorted(response_parsed, key=lambda x: x["ORPHAcode"])

def medical_specialty_orphacode_by_parent(parentcode):  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one gene.

    The result is a collection of ORPHAcodes associated to at least one gene. # noqa: E501

    """
    es = config.elastic_server
    index = "en_product7"

    query = {
        "query": {
            "term": {
                "DisorderDisorderAssociation.TargetDisorder.ORPHAcode": int(parentcode)
            }
        },
        # "_source": ["ORPHAcode"]
    }

    response = qc.multiple_res(es, index, query, size=config.scroll_size)

    return response