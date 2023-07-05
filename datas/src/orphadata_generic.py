"""

Module used to generate generic products informations from all orphadata products.

Generic product informations are written in a JSON file that has to be injected 
in an Elasticsearch instance.

"""
import argparse
from collections import OrderedDict
import json
import logging
from pathlib import Path
from typing import List, Union, Generator

try:
    from .lib.config import ROOT_DIR
    from .lib.generic_parser import GenericEsDoc
except:
    from lib.config import ROOT_DIR
    from lib.generic_parser import GenericEsDoc


FORMAT = '%(asctime)-26s %(name)-16s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
name = __name__ if __name__ != '__main__' else 'orphadata_generic'
logger = logging.getLogger(name)


def get_json_products(path: Union[str, Path], include: str='product', exclude: str='') -> List:
    """Returns list of JSON path found in the given path.
    Only JSONs with 'product' in their name are returned
    because this function is used in a module intended to 
    generate orphadata_generic.json from from all lg_product[1-9](_*).json

    Parameters
    ----------
    path : Union[str, Path]
        [description]

    Returns
    -------
    List
        [description]
    """
    if isinstance(path, str):
        path = Path(path)

    if exclude:
        return [x for x in path.glob('*.json') if include in x.stem and exclude not in x.stem]
    else: 
        return [x for x in path.glob('*.json') if include in x.stem]


def process_product3(json_files: List[Path], index: str) -> List[Union[Path, OrderedDict]]:
    product3_all = []
    for p in sorted(json_files):
        if "product3" in p.stem:
            product3_all.append(p)
            json_files.remove(p)

    if product3_all:
        logger.info("Processing {} found products 3...".format(len(product3_all)))
        product3_docs = _merge_products3(product3_all, index)
        logger.info("All products3 have been serialized into ES injectable documents.")

        # append product3 doc into list of json_files pathes
        return json_files + product3_docs
    else:
        logger.info("No product 3 has been found.")
        return json_files


def serialize_product3(json_filename: Union[str, Path], index: str) -> OrderedDict:
    if not isinstance(json_filename, Path):
        json_filename = Path(json_filename)

    doc_item = OrderedDict(
        [
            ("_index", index),
            ("Date", None),
            ("hchId", None),
            ("hchTag", None),
            ('productId', json_filename.stem),
            ("clinicalEntityNb", 0),
            ("clinicalEntities", [])
        ]
    )

    with open(json_filename, 'r') as json_file:
        for n, line in enumerate(json_file):
            if not "_index" in line:
                line_dict = json.loads(line)

                if n == 1:
                    doc_item['Date'] = line_dict['Date']
                    doc_item['hchId'] = line_dict['hch_id']
                    doc_item['hchTag'] = line_dict['hch_tag']

                doc_item['clinicalEntities'].append(
                    {
                        'ORPHAcode': line_dict["ORPHAcode"],
                        "preferredTerm": line_dict["preferredTerm"],
                    }
                )
                doc_item["clinicalEntityNb"] += 1
    
    return doc_item


def _merge_products3(json_files: List[Path], index: str='orphadata_en_product3') -> List:
    es_docs = []
    for json_filename in json_files:
        es_docs.append(serialize_product3(json_filename=json_filename, index=index))
    
    return es_docs



# def _merge_product3(json_files: List[Path], index: str):
#     merged_doc = OrderedDict(
#         [
#             ("_index", index),
#             ("_id", 'en_product3'),
#             ("productId", 'en_product3'),
#             ("productName", "Clinical classifications of rare diseases"),
#             ("Description", ''),
#             ("items", [])
#         ]
#     )

#     for json_path in json_files:
#         item = OrderedDict(
#             [
#                 ("hchId", None),
#                 ("hchTag", None),
#                 ("clinicalEntityNb", 0),
#                 ("clinicalEntities", [])
#             ]
#         )

#         with open(json_path, 'r') as json_file:
#             for n, line in enumerate(json_file):
#                 if not "_index" in line:
#                     line_dict = json.loads(line)

#                     if n == 1:
#                         item['hchId'] = line_dict['hch_id']
#                         item['hchTag'] = line_dict['hch_tag']

#                     item['clinicalEntities'].append(
#                         {
#                             'ORPHAcode': line_dict["ORPHAcode"],
#                             "PreferredTerm": line_dict["name"],
#                         }
#                     )
#                     item["clinicalEntityNb"] += 1
#         merged_doc["items"].append(item)
#     merged_doc['items'] = sorted(merged_doc['items'], key=lambda i: i["hchId"])

#     return merged_doc


def generate_docs(products_all: List[Union[Path, OrderedDict]], index: str) -> Generator:
    for product in products_all:
        if isinstance(product, Path):
            es_doc = GenericEsDoc(file_path=product, index=index)
            es_doc.fill_items()
            yield es_doc.doc
        else:
            yield product


def write_es_json(data: Generator, index: str, outdir: Union[str, Path]):
    logger.info('Writing JSON ES file for index {}...'.format(index))
    if isinstance(outdir, str):
        outdir = Path(outdir)

    with open(outdir / '{}.json'.format(index), 'w') as _json_file:
        for doc in data:
            logger.info(" - Adding document {}".format(doc['productId']))
            _index = {
                "index": {
                    "_index": doc['_index'],
                }
            }           
            _json_file.write(json.dumps(_index) + '\n')
            _json_file.write(json.dumps(doc) + '\n')


def main(input_path: Union[str, Path], index: str, outdir: Union[str, Path], include: str='product3_', exclude: str=''):
    json_filenames = get_json_products(path=input_path, include=include, exclude=exclude)
    products = process_product3(json_files=json_filenames, index=index)
    data = generate_docs(products_all=products, index=index)
    write_es_json(data=data, index=index, outdir=outdir)


def parse_args():
    parser = argparse.ArgumentParser(description='Bulk inject ORPHADATA products in ES')
    parser.add_argument(
        "-path",
        required=False,
        nargs="?",
        type=str,
        default=ROOT_DIR / 'datas' / 'json_data',
        help="Path or filename of JSON file(s)"
    )
    parser.add_argument(
        "-out",
        required=False,
        nargs="?",
        type=str,
        default=ROOT_DIR / 'datas' / 'json_data',
        help="Output path"
    )
    parser.add_argument(
        "-index",
        required=False,
        nargs="?",
        type=str,
        default='orphadata_en_product3',
        help="Name of the ES index that will be created"
    )
    parser.add_argument(
        "-include",
        required=False,
        nargs="?",
        type=str,
        default="product3_",
        help="String used to filter JSON filenames. Only JSON files containing that string will be processed (default='product')"
    )
    parser.add_argument(
        "-exclude",
        required=False,
        nargs="?",
        type=str,
        default="",
        help="String used to filter JSON filenames. Only JSON files not containing that string will be processed"
    )
    parser.add_argument('--print', action='store_true')
    
    return parser.parse_args()



if __name__ == '__main__':
    args = parse_args()

    input_path = args.path
    outdir = args.out
    index = args.index
    include = args.include
    exclude = args.exclude

    if args.print:
        logger.info("Listing of files that will be processed...")

        json_filenames = get_json_products(path=input_path, include=include, exclude=exclude)
        for _file in json_filenames:
            logger.info(' - ' + str(_file))
    else:
        main(input_path=input_path, index=index, outdir=outdir, include=include, exclude=exclude)

