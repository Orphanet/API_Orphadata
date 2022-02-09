import json
import re

"""
Provide specialized functions to treat RDcode data
"""


def clean_textual_info_RDcode(node_list):
    """
    For RDcode definition

    "SummaryInformation" in xml
    output:
    "Definition": <definition text> OR "None available"

    :param node_list: list of disorder
    :return: list of disorder with reworked textual info
    """
    # for each disorder object in the file
    for disorder in node_list:
        textual_information_list = []
        if "SummaryInformation" in disorder:
            if disorder["SummaryInformation"] is not None:
                if "TextAuto" in disorder["SummaryInformation"][0]:
                    if disorder["SummaryInformation"][0]["TextAuto"] is not None:
                        TextAuto = disorder["SummaryInformation"][0]["TextAuto"]["Info"]
                        disorder["Definition"] = TextAuto
                elif "TextSection" in disorder["SummaryInformation"][0]:
                    if disorder["SummaryInformation"][0]["TextSection"] is not None:
                        if disorder["SummaryInformation"][0]["TextSection"][0] is not None:
                            Definition = disorder["SummaryInformation"][0]["TextSection"][0]["Contents"]
                            disorder["Definition"] = Definition
                disorder.pop("SummaryInformation")
            else:
                disorder["Definition"] = "None available"
        else:
            disorder["Definition"] = "None available"
    return node_list


def insert_date(node_list, extract_date):
    """
    Append the JDBOR extract date to each disorder entry

    :param node_list: list of disorder objects
    :param extract_date: JDBOR extract date
    :return: node_list with extract date
    """
    for node in node_list:
        node["Date"] = extract_date
    return node_list


def rename_terms(node_list):
    """
    Rename some terms for RDcode

    :param node_list: list of disorder objects
    :return: node_list with renamed terms
    """
    node_list = json.dumps(node_list)

    patterns = {"\"Totalstatus\":": "\"Status\":",
                "\"Name\":": "\"Preferred term\":",
                "\"PreferredTerm\":": "\"Preferred term\":",
                # "\"GroupOfType\":": "\"ClassificationLevel\":",
                "\"ExpertLink\":": "\"OrphanetURL\":",
                "\"DisorderType\":": "\"Typology\":",
                }

    for key, value in patterns.items():
        pattern = re.compile(key)
        node_list = pattern.sub(value, node_list)

    node_list = json.loads(node_list)
    return node_list


def rework_ICD(node_list):
    """
    remove "source" from ICD external reference
    rename ExternalReference to Code ICD and reference to Code ICD10

    :param node_list:
    :return: node_list with reworked ICD reference
    """
    node_list = json.dumps(node_list)

    patterns = {"\"ExternalReference\":": "\"Code ICD\":",
                "\"Reference\":": "\"Code ICD10\":"}

    for key, value in patterns.items():
        pattern = re.compile(key)
        node_list = pattern.sub(value, node_list)

    node_list = json.loads(node_list)

    for node in node_list:
        if node["Code ICD"]:
            for index, ref in enumerate(node["Code ICD"]):
                node["Code ICD"][index].pop("Source")
    return node_list


def rework_OMIM(node_list):
    """
    remove "source" from OMIM external reference
    rename ExternalReference and reference to Code OMIM

    :param node_list:
    :return: node_list with reworked OMIM reference
    """
    node_list = json.dumps(node_list)

    patterns = {"\"ExternalReference\":": "\"Code OMIM\":",
                "\"Reference\":": "\"Code OMIM\":"}

    for key, value in patterns.items():
        pattern = re.compile(key)
        node_list = pattern.sub(value, node_list)

    node_list = json.loads(node_list)

    for node in node_list:
        if node["Code OMIM"]:
            for index, ref in enumerate(node["Code OMIM"]):
                node["Code OMIM"][index].pop("Source")

    return node_list