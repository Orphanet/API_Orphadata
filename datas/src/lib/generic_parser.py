import json
from pathlib import Path
from typing import Dict, List

from .config import PRODUCT_DEF


class GenericEsDoc:
    def __init__(self, file_path: Path, index) -> None:
        self.file_path = file_path
        self.product_id = file_path.stem
        self.product_type = file_path.stem.split('_')[1]
        self.product_name = PRODUCT_DEF[self.product_type]
        self.itemParser = ITEM_PARSERS[self.product_type]

        self.doc = {
            "_index": index,
            "_id": self.product_id,
            "productId": self.product_id,
            "productName": self.product_name,
            "description": '',
            "items": []
        }

    def fill_items(self):
        with open(self.file_path, 'r') as json_file:
            for line in json_file:
                if "ORPHAcode" in line: 
                    line_dict = json.loads(line)
                    self.doc['items'].append(
                        self.itemParser.get_infos(line_dict=line_dict)
                    )

    def dump(self, indent=2):
        return json.dumps(self.doc, indent=indent)

    def log_parser(self):
        return self.itemParser.logs


class ParserCheckMixin:
    logs = []

    def check_missing(self, items: Dict, line_dict: Dict):
        missing_values = []
        for key in items:
            if not items[key]:
                missing_values.append('missing value for key "{}"'.format(key))
        
        if missing_values:
            self.logs.append({'missing': missing_values, 'line': line_dict})


class ItemParserProduct(ParserCheckMixin):  
    def get_infos(self, line_dict: Dict):
        items = {
            "ORPHAcode": line_dict["ORPHAcode"] or None,
            "preferredTerm": line_dict["Preferred term"] or None
        }

        self.check_missing(items, line_dict)
        return items


class ItemParserProduct1(ParserCheckMixin):
    def get_infos(self, line_dict: Dict):
        items = {
                "ORPHAcode": line_dict["ORPHAcode"],
                "preferredTerm": line_dict["Preferred term"],
                "externalReference": []
                }

        if line_dict['ExternalReference']:        
            omim_lst = [ x['Reference'] for x in line_dict['ExternalReference'] if x['Source'] == 'OMIM' ]
            icd_lst = [ x['Reference'] for x in line_dict['ExternalReference'] if x['Source'] == 'ICD-10' ]

            items["externalReference"].append(
                {
                    "OMIMList": [ x for x in omim_lst],
                    "ICD-10List": [ x for x in icd_lst],
                }
            )            


        self.check_missing(items, line_dict)
        return items


class ItemParserProduct3(ParserCheckMixin):
    """
    #TODO PreferredTerm or Name?
    """
    def get_infos(self, line_dict: Dict):
        items = {
                "ORPHAcode": line_dict["ORPHAcode"] or None,
                "preferredTerm": line_dict["name"] or None,
                "hchId": line_dict["hch_id"] or None,
                "hchTag": line_dict["hch_tag"] or None
                }

        self.check_missing(items, line_dict)
        return items


class ItemParserProduct4(ParserCheckMixin):
    def get_infos(self, line_dict: Dict):
        items = {
                "ORPHAcode": line_dict["Disorder"]["ORPHAcode"] or None,
                "preferredTerm": line_dict["Disorder"]["Preferred term"] or None,
                "associatedHPOs": []
                }

        if line_dict["Disorder"]['HPODisorderAssociation']:        
            for associated_hpos in line_dict["Disorder"]['HPODisorderAssociation']:
                hpo_id = associated_hpos['HPO']['HPOId']
                hpo_term = associated_hpos['HPO']['HPOTerm']
                hpo_frequency = associated_hpos['HPOFrequency']

                items["associatedHPOs"].append(
                    {
                        "HPOId": hpo_id,
                        "HPOTerm": hpo_term,
                        "HPOFrequency": hpo_frequency
                    }
                )

        self.check_missing(items, line_dict)
        return items


class ItemParserProduct6(ParserCheckMixin):
    def get_infos(self, line_dict: Dict):
        items = {
                "ORPHAcode": line_dict["ORPHAcode"],
                "preferredTerm": line_dict["Preferred term"],
                "associatedGenes": []
                }

        if line_dict['DisorderGeneAssociation']:        
            for associated_genes in line_dict['DisorderGeneAssociation']:
                gene_name = associated_genes['Gene']['Preferred term']
                gene_symbol = associated_genes['Gene']['Symbol']

                if associated_genes['Gene']['ExternalReference']:
                    hgnc_lst = [ x['Reference'] for x in associated_genes['Gene']['ExternalReference'] if x['Source'] == 'HGNC' ]
                    if hgnc_lst:
                        items["associatedGenes"].append(
                            {
                                "geneName": gene_name,
                                "geneSymbol": gene_symbol,
                                "HGNC": hgnc_lst[0]
                            }
                        )   

        self.check_missing(items, line_dict)
        return items


class ItemParserProduct7(ParserCheckMixin):
    """
    @BUG? why a list for preferential parent?
    @BUG? 2 orphacodes with missing parents: 610573, 610569
    """
    def get_infos(self, line_dict: Dict):
        items = {
                "ORPHAcode": line_dict["ORPHAcode"],
                "preferredTerm": line_dict["Preferred term"],
                "preferentialParent": []
                }

        if line_dict['DisorderDisorderAssociation']:
            for parent in line_dict['DisorderDisorderAssociation']:
                orphacode = parent['TargetDisorder']['ORPHAcode']
                preferred_term = parent['TargetDisorder']['Preferred term']

                items["preferentialParent"].append(
                    {
                        "ORPHAcode": orphacode,
                        "preferredTerm": preferred_term,
                    }
                )

        self.check_missing(items, line_dict)
        return items


class ItemParserProduct9(ItemParserProduct):
    pass


ITEM_PARSERS = {
    'product1': ItemParserProduct1(),
    'product3': ItemParserProduct3(),
    'product4': ItemParserProduct4(),
    'product6': ItemParserProduct6(),
    'product7': ItemParserProduct7(),
    'product9': ItemParserProduct9(),
}


