"""

Module used to convert each orphadata XML file in JSON format.

JSON files represent the inputs to be injected in Elasticsearch instance.

"""

import copy
import elasticsearch
import json
import logging
import re
import time
import xmltodict
import os
from tqdm import tqdm


FORMAT = '%(asctime)-26s %(name)-26s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
name = __name__ if __name__ != '__main__' else 'orphadata_xml2json'
logger = logging.getLogger(name)


import orphadata_generic

from lib.config import ROOT_DIR
from lib import data_RDcode
from lib import RDcode_classifications
from lib import orphadata_classifications


class XML2JSONParams:
    in_file_path = None  # pathlib.Path(ROOT_DIR / 'datas' / 'en_product1.xml')
    parse_folder = True if not in_file_path else False  # Process all input folders or single input file ?
    folders = [ROOT_DIR / 'datas' / 'xml_data']  # List of path to folder containing data
    out_folder = ROOT_DIR / 'datas' / 'json_data'
    input_encoding = "auto"  # input encoding: "auto" or valid encoding ("UTF-8" or "iso-8859-1")
    index_prefix = ""  # Empty string or False otherwise - The prefix MUST be 'rdcode' for RDcode API (lowercase index name is mandatory)
    cast_as_integer = True  # Remap number as integer
    indent_output = False  # Indent output file (True for visual data control, need to be False for elasticsearch upload)
    upload = False  # Upload to elasticsearch node if true
    make_schema = False  # Make the yaml schema description
    output_encoding = "UTF-8"


config = XML2JSONParams()


def parse_file(in_file_path, input_encoding, xml_attribs):
    """
    Parse an xml file with "xmltodict" external module and return the file as a dictionary and the extraction date.
    Can read the encoding of the file in the xml header if input_encoding=="auto" OR decode the file with
    the specified encoding.
    Can read the JDBOR extraction date in the xml attribute of the JDBOR node but the rest of the code is meant to
    work without the xml attributes to read them call with xml_attribs=True.

    :param in_file_path: path, source xml file
    :param input_encoding: valid encoding OR "auto"
    :param xml_attribs: Boolean, read the xml attribute such as "id" in <Disorder id="12948"> ?
    :return: tuple(xml_dict, extraction date)
        WHERE
        xml_dict: xml source file parsed as a dictionary
        extraction date: str, date of JDBOR extraction
    """
    start = time.time()

    # Encoding detection
    with open(in_file_path, "rb") as ini:
        xml_declaration = ini.readline()
        date = ini.readline()

    if input_encoding.lower() == "auto":
        xml_declaration = xml_declaration.decode()
        pattern = re.compile("encoding=\"(.*)\"[ ?]")
        encoding = pattern.search(xml_declaration).group(1)
        logger.info('encoding: {} (auto)'.format(encoding))

        with open(in_file_path, "r", encoding=encoding) as ini:
            xml_dict = xmltodict.parse(ini.read(), xml_attribs=xml_attribs)

    else:
        with open(in_file_path, "r", encoding=input_encoding) as ini:
            logger.info('encoding: {} (from config file)'.format(input_encoding))
            xml_dict = xmltodict.parse(ini.read(), xml_attribs=xml_attribs)

    # Get JDBOR extraction date
    date_regex = re.compile("date=\"(.*)\" version")
    date = date_regex.search(date.decode()).group(1)
    logger.info("JDBOR extract: {}".format(date))

    # print(xml_dict)
    # DumpS then loadS: convert ordered dict to dict
    # xml_dict = json.loads(json.dumps(xml_dict, ensure_ascii=False))
    logger.info("parsing: {}".format(time.time() - start))
    return xml_dict, date


def subset_xml_dict(xml_dict):
    """
    Reroot the xml to skip the trivial JDBOR/*List/ for homogeneity (ClassificationList vs DisorderList)

    :param xml_dict: xml source file parsed as a dictionary
    :return: xml source file parsed as a dictionary rerooted to the first *List
    """
    # Return the first meaningful node for homogeneity
    key = list(xml_dict["JDBOR"].keys())
    if "Availability" in key:
        key.pop(key.index("Availability"))

    new_key = []
    for item in key:
        # the xml attribute are prefixed with @ and can be discarded for application
        if "@" not in item:
            new_key.append(item)
    # print(key)
    if len(new_key) == 1:
        new_key = new_key[0]
    else:
        logger.error("ERROR: Multiple root XML key: {}".format(new_key))
        exit(1)

    xml_dict = xml_dict["JDBOR"][new_key]
    return xml_dict


def simplify_xml_list(xml_dict):
    """
    Recursively simplify the xml structure for homogeneity
    Remove
    <ClassificationNodeList count="XX">
        <ClassificationNode>
            <ClassificationNodeChildList count="XX">
    To produce
    ClassificationNode: [{*current node information*, ClassificationNodeChild: {}}, ...]

    :param xml_dict: xml source file parsed as a dictionary
    :return: simplified xml_dict
    """
    if isinstance(xml_dict, dict):
        for key, elem in xml_dict.items():
            if key.endswith("List"):
                xml_dict = simplify_list(xml_dict, key)
            simplify_xml_list(elem)
    elif isinstance(xml_dict, list):
        for elem_list in xml_dict:
            simplify_xml_list(elem_list)
    return xml_dict


def simplify_list(parent, key):
    """
    Remove trivial key and regroup it's children as a "child" property of the trivial key's parent
    Properly map empty children as 'None'

    :param parent: Dictionary containing key to simplify
    :param key: Dictionary key containing the term "*List"
    :return: simplified dictionary
    """
    child_value = parent[key]
    if child_value is not None and child_value != "0":
        child_value = [child_value[child] for child in child_value if child][0]
        if isinstance(child_value, dict) or isinstance(child_value, str):
            child_value = [child_value]
        parent[key] = child_value
    else:
        parent[key] = None
    return parent


def merge_unique(list1, list2):
    """
    Merge two list and keep unique values
    """
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1


def simplify(xml_dict, rename_orpha):
    """
    :param xml_dict: xml source file parsed as a dictionary
    :param rename_orpha: boolean, force the conversion of ALL OrphaNumber/i or OrphaCode/i to ORPHAcode
    :return: node_list: List of Disorder object with simplified structure
    i.e.:
    [{
        "name": "Congenital pericardium anomaly",
        "ORPHAcode": "2846",
        "hch_id": "148",
        "parents": ["97965"],
        "childs": ["99129", "99130", "99131"]
    },
    {...}
    ]
    """
    # start = time.time()

    # Simplify the xml structure for homogeneity
    xml_dict = simplify_xml_list(xml_dict)

    # print(xml_dict)
    # output_simplified_dictionary(out_file_path, index, xml_dict)

    key = list(xml_dict.keys())
    # print(key)

    if len(key) == 1:
        key = key[0]
    else:
        logger.error("ERROR: Multiple root XML key: {}".format(key))
        exit(1)

    node_list = xml_dict[key]
    node_list = json.dumps(node_list, ensure_ascii=False)

    pattern = re.compile("List\":")
    node_list = pattern.sub("\":", node_list)
    if rename_orpha:
        pattern = re.compile("OrphaCode", re.IGNORECASE)
        node_list = pattern.sub("ORPHAcode", node_list)
        pattern = re.compile("OrphaNumber", re.IGNORECASE)
        node_list = pattern.sub("ORPHAcode", node_list)
    node_list = json.loads(node_list)

    logger.info("Disorder concepts number: {}".format(len(node_list)))
    return node_list


def recursive_template(elem):
    if isinstance(elem, dict):
        for child in elem:
            recursive_template(child)
    elif isinstance(elem, list):
        for sub_elem in elem:
            recursive_template(sub_elem)
    return elem


def recursive_unwanted_orphacode(elem):
    """
    Remove the ORPHAcode past the one defined at the disorder's root level
    ! NO quality check !
    Useless since new Orphadata generation

    :param elem: disorder object or property
    :return: disorder object or property without ORPHAcode key
    """
    if isinstance(elem, dict):
        if "ORPHAcode" in elem.keys():
            elem.pop("ORPHAcode")
        for child in elem:
            recursive_unwanted_orphacode(elem[child])
    elif isinstance(elem, list):
        for sub_elem in elem:
            recursive_unwanted_orphacode(sub_elem)
    return elem


def remove_unwanted_orphacode(node_list):
    """
    Remove the ORPHAcode past the one defined at the disorder's root level
    ! NO quality check !
    Useless since new Orphadata generation

    :param node_list: list of disorder
    :return: list of disorder without ORPHAcode key past the main one
    """
    for disorder in node_list:
        # elem is an attribute of the disorder
        for elem in disorder:
            recursive_unwanted_orphacode(disorder[elem])
    return node_list


def clean_textual_info(node_list):
    """
    For product 1 (cross references)

    "SummaryInformation" in xml
    output:
    "SummaryInformation": [{"Definition": "definition text"}, {"info": "automatic definition text"}]
    Definition AND info key are both optional, in this case SummaryInformation: None

    :param node_list: list of disorder
    :return: list of disorder with reworked textual info
    """
    # for each disorder object in the file
    for disorder in node_list:
        TextAuto = ""
        textual_information_list = []
        if "TextAuto" in disorder:
            temp = {}
            TextAuto = disorder["TextAuto"]["Info"]
            temp["Info"] = TextAuto
            textual_information_list.append(temp)
            disorder.pop("TextAuto")
        if "SummaryInformation" in disorder:
            if disorder["SummaryInformation"] is not None:
                for text in disorder["SummaryInformation"]:
                    if text["TextSection"] is not None:
                        temp = {}
                        key = text["TextSection"][0]["TextSectionType"]["Name"]
                        temp[key] = text["TextSection"][0]["Contents"]
                        textual_information_list.append(temp)
            if textual_information_list:
                disorder["SummaryInformation"] = textual_information_list
            else:
                disorder["SummaryInformation"] = None
        else:
            disorder["SummaryInformation"] = None
    return node_list


def recursive_clean_single_name_object(elem):
    """
    Take the list of disorder and substitute object by a text if they contain only one "Name" property
    keeps multi-property object otherwise
    i.e.:
    disorder["DisorderType"]["Name"] = "Disease"
    to =>
    disorder["DisorderType"] = "Disease"
    Work in depth recursively
    :param elem: property of disorder
    :return: list of disorder without single name object
    """
    if isinstance(elem, dict):
        keys = elem.keys()
        if len(keys) == 1:
            if "Name" in keys:
                name = elem.pop("Name")
                elem = name
        else:
            for child in elem:
                elem[child] = recursive_clean_single_name_object(elem[child])
    elif isinstance(elem, list):
        for index, sub_elem in enumerate(elem):
            sub_elem = recursive_clean_single_name_object(sub_elem)
            elem[index] = sub_elem
    return elem


def clean_single_name_object(node_list):
    """
    Take the list of disorder and substitute object by a text if they contain only one "Name" property
    keeps multi-property object otherwise
    i.e.:
    disorder["DisorderType"]["Name"] = "Disease"
    to =>
    disorder["DisorderType"] = "Disease"
    Work in depth recursively
    :param node_list: list of disorder
    :return: list of disorder without single name object
    """
    for disorder in node_list:
        for elem in disorder:
            disorder[elem] = recursive_clean_single_name_object(disorder[elem])
    return node_list


def gene_indexing(node_list_gene):
    """
    Invert the indexing of the product6 "gene" to index the relationships between gene and disorder
    from the gene point of view

    :param node_list_gene: copy of processed node_list
    :return: similar list of disorder-gene relation but indexed by gene
    ie.
    [
    {
    "Name": "kinesin family member 7",
    "Symbol": "KIF7",
    "Synonym": [
        "JBTS12"
    ],
    "GeneType": "gene with protein product",
    "ExternalReference": [
        {
        "Source": "Ensembl",
        "Reference": "ENSG00000166813"
        },
        {...},
    ],
    "Locus": [
        {
        "GeneLocus": "15q26.1",
        "LocusKey": "1"
        }
    ],
    "GeneDisorderAssociation": [
        {
        "SourceOfValidation": "22587682[PMID]",
        "DisorderGeneAssociationType": "Disease-causing germline mutation(s) in",
        "DisorderGeneAssociationStatus": "Assessed",
        "disorder": {
            "ORPHAcode": "166024",
            "ExpertLink": "http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=166024",
            "Name": "Multiple epiphyseal dysplasia, Al-Gazali type",
            "DisorderType": "Disease",
            "DisorderGroup": "Disorder"
        }
        },
        {...}
    ]
    }
    ]
    """
    gene_dict = dict()
    for disorder in node_list_gene:
        # disorder still contains gene association
        disorder_info = copy.deepcopy(disorder)

        # association_list : list, need to exploit with according gene
        # disorder_info now only contains disorder
        association_list = disorder_info.pop("DisorderGeneAssociation")

        for association_info in association_list:
            # Each association_info contains a different Gene,
            # we need to index the Gene then substitute it with disorder_info
            gene_info = association_info.pop("Gene")
            gene_index = gene_info["Symbol"]
            # Initialize the Gene index on first occurrence
            if gene_index not in gene_dict:
                gene_dict[gene_index] = {}
                for gene_prop, gene_prop_value in gene_info.items():
                    gene_dict[gene_index][gene_prop] = gene_prop_value
                gene_dict[gene_index]["GeneDisorderAssociation"] = []
            # insert disorder_info in the association_info
            association_info["disorder"] = disorder_info
            # Extend the GeneDisorderAssociation with this new disorder relation
            gene_dict[gene_index]["GeneDisorderAssociation"].append(association_info)

    node_list_gene = list(gene_dict.values())
    return node_list_gene


def output_simplified_dictionary(out_file_path, index, xml_dict, indent_output, output_encoding):
    """
    Output simplified dictionary in json format DEBUG helper function

    Simplified the xml structure to give a consistent hierarchy:
    Disorder: {}
    Child: [
        {
        Disorder: {}
        Child: []
        },
        {
        Disorder: {}
        Child: []
        }
    ]

    :param out_file_path: path to output file
    :param index: name of the elasticsearch index
    :param xml_dict: xml source file parsed as a dictionary
    :return: None
    """
    if indent_output:
        indent = 2
    else:
        indent = None
    with open(out_file_path, "w", encoding=output_encoding) as out:
        out.write("{{\"index\": {{\"_index\":\"{}\"}}}}\n".format(index))
        out.write(json.dumps(xml_dict, indent=indent, ensure_ascii=False) + "\n")


def output_elasticsearch_file(out_file_path, index, node_list, indent_output, output_encoding):
    """
    Output json file, elasticsearch injection ready

    :param out_file_path: path to output file
    :param index: name of the elasticsearch index
    :param node_list: list of Disorder, each will form an elasticsearch document
    :param indent_output: if True, will pretty print with indent = 2 ; MUST be false for ES upload or schema description
    :param output_encoding: "UTF-8" or "iso-8859-1"
    :return: None
    """
    start = time.time()
    if indent_output:
        indent = 2
    else:
        indent = None
    with open(out_file_path, "w", encoding=output_encoding) as out:
        for val in node_list:
            out.write("{{\"index\": {{\"_index\":\"orphadata_{}\"}}}}\n".format(index))
            out.write(json.dumps(val, indent=indent, ensure_ascii=False) + "\n")
    logger.info("writing time: {}s".format(time.time() - start))


def upload_es(elastic, processed_json_file):
    """
    Upload processed json file to elasticsearch node

    :param elastic: URI to elastic node, False otherwise
    :param processed_json_file: path
    :return: None
    """
    start = time.time()
    full_file = processed_json_file.read_text(encoding="UTF-8")

    try:
        ES_response = elastic.bulk(body=full_file)
        if ES_response["errors"]:
            err_doc_ids = [ x for x in range(len(ES_response["items"])) if ES_response["items"][x]["index"]["status"] != 201 ]
            err_log = "{} ES upload ERROR(S) with {}".format(len(err_doc_ids), processed_json_file.name)
            print("\n" + err_log)
            print("-"*len(err_log))

            for err_doc_id in err_doc_ids:
                print(json.dumps(ES_response["items"][err_doc_id]["index"]["error"], indent=2))
            exit(1)
    except elasticsearch.exceptions.ConnectionError:
        logger.error("ERROR: elasticsearch node unavailable")
        exit(1)
    print("upload ES:", time.time() - start, "s")


def remap_integer(node_list):
    """
    Cast number as integer (from string) using regex
    SKIP number preceded by "Reference: "

    :param node_list: list of disorder
    :return:
    """
    node_list = json.dumps(node_list)

    def hexrepl(match):
        """ Replace function for the capture group """
        value = match.group()[1:-1]
        return value

    pattern = re.compile("(?<!Reference\":\\s)\"\\d+\"")
    node_list = pattern.sub(hexrepl, node_list)

    node_list = json.loads(node_list)
    return node_list


def process(in_file_path, out_folder, elastic, input_encoding, indent_output, output_encoding):
    """
    Complete Orphadata XML to Elasticsearch JSON process

    :param in_file_path: input file path
    :param out_folder: output folder path
    :param elastic: URI to elastic node, False otherwise
    :param input_encoding: str, valid encoding or "auto"
    :param indent_output: boolean, indent entry in output file with 2 spaces
    :param output_encoding: str, valid encoding
    :return: None (Write file (mandatory) / upload to elastic cluster)
    """
    file_stem = in_file_path.stem.lower()
    if "CZ" in file_stem:
        file_stem = file_stem.replace("CZ", "CS")
    if "cz" in file_stem:
        file_stem = file_stem.replace("cz", "cs")
    # Remove the suffixed date
    file_stem = re.sub("_[0-9]{4}(?![0-9])", "", file_stem)

    index = config.index_prefix
    if index:
        index = "{}_{}".format(index, file_stem)
    else:
        index = file_stem
    logger.info("####################")
    logger.info('file stem:  {}'.format(file_stem))
    out_file_name = index + ".json"
    out_file_path = out_folder / out_file_name

    # Parse source xml file and return the date also reroot the xml to skip the trivial JDBOR/*List/
    xml_dict, extract_date = parse_file(in_file_path, input_encoding, False)
    xml_dict = subset_xml_dict(xml_dict)

    start = time.time()
    # remove intermediary dictionary (xml conversion artifact) and rename OrphaNumber
    rename_orpha = True  # OrphaNumber to ORPHAcode
    node_list = simplify(xml_dict, rename_orpha)

    # Output this simplified dictionnary for debug purpose
    # output_simplified_dictionary(out_file_path, index, node_list, indent_output, output_encoding)

    # Useless since new Orphadata generation
    # Remove orphacode past the main one (/!\ NO QUALITY CHECK)
    # node_list = remove_unwanted_orphacode(node_list)

    # Regroup textual_info for product1 or RDcode orphanomenclature
    if "product1" in file_stem:
        node_list = clean_textual_info(node_list)
    if "orphanomenclature" in file_stem:
        node_list = data_RDcode.clean_textual_info_RDcode(node_list)

    # Remap object with single "Name" to string
    node_list = clean_single_name_object(node_list)

    # Cast number as integer (from string)
    if config.cast_as_integer:
        node_list = remap_integer(node_list)

    # # Index product6 "gene" by gene symbol
    # if "product6" in file_stem:
    #     node_list_gene = copy.deepcopy(node_list)
    #     node_list_gene = gene_indexing(node_list_gene)
    #     out_file_path_gene = pathlib.Path(str(out_file_path.absolute()).split(".")[0] + "_gene" + out_file_path.suffix)
    #     index_gene = out_file_path_gene.stem
    #     # Output/upload function
    #     output_process(out_file_path_gene, index_gene, node_list_gene, elastic, indent_output, output_encoding)

    # For RDcode API, insert date /!\ RDcode classification got its own process module
    if "orphanomenclature" in file_stem or "orpha_icd10_" or "orpha_omim_" in file_stem:
        node_list = data_RDcode.insert_date(node_list, extract_date)
        node_list = data_RDcode.rename_terms(node_list)
    if "orpha_icd10_" in file_stem:
        node_list = data_RDcode.rework_ICD(node_list)
    if "orpha_omim_" in file_stem:
        node_list = data_RDcode.rework_OMIM(node_list)

    logger.info("convert time: {}s".format(time.time() - start))

    # Output/upload function
    output_process(out_file_path, index, node_list, elastic, indent_output, output_encoding)


def output_process(out_file_path, index, node_list, elastic, indent_output, output_encoding):
    """
    Output processed node list in elasticsearch JSON and eventually upload the file to "elastic" URI

    :param out_file_path: path
    :param index: index name that will be in elasticsearch indexing instruction
    :param node_list: collection of Disorder (Orphanet concept) object
    :param elastic: URI to elastic node, False otherwise
    :param indent_output: Indent output file (True for visual data control, MUST be False for elasticsearch upload)
    :param output_encoding:
    :return: None
    """
    # Output a json elasticsearch ready, with index name as indexing instruction
    output_elasticsearch_file(out_file_path, index, node_list, indent_output, output_encoding)
    logger.info('')

    if elastic:
        # Upload to elasticsearch node
        upload_es(elastic, out_file_path)
        logger.info('')

    if config.make_schema:
        if out_file_path.stem.startswith("en"):
            if "product3" in out_file_path.stem:
                if out_file_path.stem.endswith("146"):
                    yaml_schema_descriptor.yaml_schema(config.out_folder, out_file_path, output_encoding)
            else:
                yaml_schema_descriptor.yaml_schema(config.out_folder, out_file_path, output_encoding)
        logger.info('')


def write_generic_product3():
    orphadata_generic.main(input_path=config.out_folder, index='orphadata_en_product3', outdir=config.out_folder, include='product3_')

def main():
    # Some config check
    if config.indent_output:
        if config.upload:
            logger.error('ERROR: Bad configuration indent_output {} and upload {} should be mutually exclusive:'.format(config.indent_output, config.upload))
        if config.make_schema:
            logger.error('ERROR: Bad configuration indent_output {} and make_schema {} should be mutually exclusive:'.format(config.indent_output, config.make_schema))
        if config.upload or config.make_schema:
            exit(1)

    if config.upload:
        elastic = config.elastic_node
    else:
        elastic = False
    logger.info('')

    os.makedirs(config.out_folder, exist_ok=True)


    if config.parse_folder:

        _notqdm = True if __name__ == '__main__' else False

        # Process files in designated folders
        for folder in config.folders:            
            for file in tqdm(iterable=folder.iterdir(), desc="JSON converted XML files", total=len(list(folder.iterdir())), disable=_notqdm):
                if not file.is_dir():
                    if file.suffix == ".xml":                     
                        if "product3" in file.stem:
                            orphadata_classifications.process_classification(
                                file,
                                config.out_folder,
                                elastic,
                                config.input_encoding,
                                config.indent_output,
                                config.output_encoding
                            )
                        elif "ORPHAclassification" in file.stem:
                            RDcode_classifications.process_classification(
                                file,
                                config.out_folder,
                                elastic,
                                config.input_encoding,
                                config.indent_output,
                                config.output_encoding
                            )
                        else:
                            process(
                                file,
                                config.out_folder,
                                elastic,
                                config.input_encoding,
                                config.indent_output,
                                config.output_encoding
                            )

    else:
        # Process single file
        file = config.in_file_path
        if "product3" in file.stem:
            orphadata_classifications.process_classification(
                file,
                config.out_folder,
                elastic,
                config.input_encoding,
                config.indent_output,
                config.output_encoding
            )
        elif "ORPHAclassification" in file.stem:
            RDcode_classifications.process_classification(
                file,
                config.out_folder,
                elastic,
                config.input_encoding,
                config.indent_output,
                config.output_encoding
            )
        else:
            process(
                file,
                config.out_folder,
                elastic,
                config.input_encoding,
                config.indent_output,
                config.output_encoding
            )

    write_generic_product3()

if __name__ == "__main__":
    start = time.time()
    main()
    logger.info('Total computation time: {}s'.format(time.time() - start))
