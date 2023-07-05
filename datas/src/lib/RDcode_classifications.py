import re
import time

from . import data_RDcode
import orphadata_xml2json


"""
Alternative process to treat RDcode classification
"""


class Node(dict):
    def __init__(self):
        super().__init__()
        self["Preferred term"] = ""
        self["ORPHAcode"] = ""
        self["Classification"] = {}
        self["Classification"]["ID of the classification"] = ""
        self["Classification"]["ORPHAcode"] = ""
        self["Classification"]["Name of the classification"] = ""
        self["Classification"]["Preferred term"] = ""
        self["Parent"] = []
        self["Child"] = []


def parse_plator(pat_hch_path):
    """
    Parse PatHch.Txt (plator extract) to create a dictionary to convert hch_id to hch_tag
    DEPRECATED: classification xml now output the hch label

    :param pat_hch_path:
    :return: hch_dict: dictionary to convert hch_id to hch_tag
    """
    hch_dict = {}
    with open(pat_hch_path, "r") as ini:
        header = ini.readline()[:-1].split("\t")
        hch_id_index = header.index("HchId")
        hch_tag_index = header.index("HchTag (english label)")
        lng_index = header.index("Lng")
        for line in ini:
            data = line[:-1].split("\t")
            if data[lng_index] == "en":
                hch_dict[data[hch_id_index]] = data[hch_tag_index]
    # print(hch_dict)
    return hch_dict


def make_node_dict(node_dict, xml_dict, hch_id, hch_tag, parent, classification_orpha):
    """
    Recursively parse xml_dict to output a collection of Disorder with all their children

    :param node_dict: Dictionary of Disorders i.e.
    {2846: {
        "Preferred term": "Congenital pericardium anomaly",
        "OrphaNumber": "2846",
        "hch_id": "148",
        "Parent": ["97965"],
        "Child": ["99129", "99130", "99131"]
        },
    2847: {...}
    }
    :param hch_id: String, Orphanet classification number
    :param hch_tag: String, Orphanet classification tag
    :param xml_dict: xml source file parsed as a dictionary
    :param parent: Orpha_ID of parent Disorder
    :param classification_orpha: Orpha_ID of classification
    :return: node_dict
    """
    # print(xml_dict)
    node = Node()
    node["ORPHAcode"] = xml_dict["Disorder"]["ORPHAcode"]
    node["Preferred term"] = xml_dict["Disorder"]["Name"]
    node["Classification"]["ORPHAcode"] = classification_orpha
    node["Classification"]["ID of the classification"] = hch_id
    node["Classification"]["Name of the classification"] = hch_tag
    node["Classification"]["Preferred term"] = hch_tag
    node["Parent"] = [parent]
    # print(node)
    if xml_dict["ClassificationNodeChild"] is not None:
        for child in xml_dict["ClassificationNodeChild"]:
            node["Child"].append(child["Disorder"]["ORPHAcode"])
            node_dict = make_node_dict(node_dict, child, hch_id, hch_tag, node["ORPHAcode"], classification_orpha)
    if node["ORPHAcode"] in node_dict:
        node_dict[node["ORPHAcode"]]["Child"] = merge_unique(node_dict[node["ORPHAcode"]]["Child"], node["Child"])
        node_dict[node["ORPHAcode"]]["Parent"] = merge_unique(node_dict[node["ORPHAcode"]]["Parent"], node["Parent"])
        # print(node_dict[node.OrphaNumber].Child)
    else:
        node_dict[node["ORPHAcode"]] = node
    return node_dict


def merge_unique(list1, list2):
    """
    Merge two list and keep unique values
    """
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1


def convert(hch_id, xml_dict, classification_orpha):
    """
    :param hch_id: String, Orphanet classification number
    :param xml_dict: xml source file parsed as a dictionary
    :param classification_orpha: Orpha_ID of classification
    :return: node_list: List collection of Disorder
    i.e.:
    [
    {"Preferred term": "Congenital pericardium anomaly",
    "OrphaNumber": "2846",
    "hch_id": "148",
    "Parent": ["97965"],
    "Child": ["99129", "99130", "99131"]
    },
    {...}
    ]
    """
    start = time.time()
    # With 2020 dataset the Orphanet classification level appear in the file, it contain only the OrphaNumber(ORPHAcode)
    # and the name, we need to capture this special case
    try:
        disorder = {'ORPHAcode': xml_dict["ORPHAcode"], 'ExpertLink': xml_dict["ExpertLink"], 'Name': xml_dict["Name"]}
    except KeyError:
        disorder = {'ORPHAcode': xml_dict["ORPHAcode"], 'ExpertLink': "", 'Name': xml_dict["Name"]}

    # With 2020 dataset the Orphanet classification level appear in the file, it has a scpecial label for hierarchy,
    # we need to capture this special case
    try:
        ClassificationNodeChild = xml_dict["ClassificationNode"][0]["ClassificationNodeChild"]
    except KeyError:
        ClassificationNodeChild = xml_dict["ClassificationNodeRoot"]

    xml_dict = {"Disorder": disorder, "ClassificationNodeChild": ClassificationNodeChild}

    hch_tag = xml_dict["Disorder"]["Name"]
    parent = None

    node_dict = {}
    node_dict = make_node_dict(node_dict, xml_dict, hch_id, hch_tag, parent, classification_orpha)

    node_list = list(node_dict.values())

    # print(node_list)
    print(len(node_list), "disorder concepts")

    print(time.time() - start, "s")
    return node_list


def process_classification(in_file_path, out_folder, elastic, input_encoding, indent_output, output_encoding):
    """
    Complete Orphadata XML to Elasticsearch JSON process

    :param in_file_path: input file path
    :param out_folder: output folder path
    :param elastic: URI to elastic node, False otherwise
    :param input_encoding:
    :param indent_output: indent output file (True for visual data control, MUST be False for elasticsearch upload)
    :param output_encoding:
    :return: None (Write file (mandatory) / upload to elastic cluster)
    """

    file_stem = in_file_path.stem.lower()
    if "CZ" in file_stem:
        file_stem = file_stem.replace("CZ", "CS")
    if "cz" in file_stem:
        file_stem = file_stem.replace("cz", "cs")

    # Remove the suffixed date
    file_stem = re.sub("_[0-9]{4}(?![0-9])", "", file_stem)

    file_stem_split = file_stem.split("_")
    # remove classification name from input path
    # orphaclassification_146_rare_cardiac_disease_en
    # TO
    # orphaclassification_146_en
    file_stem = "{}_{}_{}".format(file_stem_split[0], file_stem_split[1], file_stem_split[-1])
    index = orphadata_xml2json.config.index_prefix
    if index:
        index = "{}_{}".format(index, file_stem)
    else:
        index = file_stem
    print(file_stem)
    out_file_name = index + ".json"
    out_file_path = out_folder / out_file_name

    hch_id = file_stem.split("_")[1]

    # Parse source xml file with xml attributes
    # xml_dict, extract_date = orphadata_xml2json.parse_file(in_file_path, input_encoding, True)
    # classification_id = xml_dict["Disorder"]["@id"]
    # classification_orpha = xml_dict["Disorder"]["OrphaNumber"]

    # Parse source xml file and return the date also reroot the xml to skip the trivial JDBOR/*List/
    xml_dict, extract_date = orphadata_xml2json.parse_file(in_file_path, input_encoding, False)
    xml_dict = orphadata_xml2json.subset_xml_dict(xml_dict)

    classification_orpha = xml_dict["Classification"]["OrphaNumber"]

    start = time.time()
    # remove intermediary dictionary (xml conversion artifact) and rename OrphaNumber
    rename_orpha = True  # OrphaNumber to ORPHAcode
    xml_dict = orphadata_xml2json.simplify(xml_dict, rename_orpha)

    node_list = convert(hch_id, xml_dict, classification_orpha)

    node_list = data_RDcode.insert_date(node_list, extract_date)

    if orphadata_xml2json.config.cast_as_integer:
        node_list = orphadata_xml2json.remap_integer(node_list)

    print("convert:", time.time() - start, "s")

    # Output/upload function
    orphadata_xml2json.output_process(out_file_path, index, node_list, elastic, indent_output, output_encoding)
