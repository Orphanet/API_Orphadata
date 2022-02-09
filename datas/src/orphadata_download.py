"""

Module used to download XML orphadata products. 

XML file URLs are retrieved from product-related JSONs 
located in http://www.orphadata.org/cgi-bin/...

"""
import logging
from pathlib import Path
from typing import Dict, Union, List
import requests
import os

from lib.config import ROOT_DIR, PATH_PRODUCTS_INFOS


FORMAT = '%(asctime)-26s %(name)-26s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('download_orphadata')

OUTPATH = Path(ROOT_DIR) / 'datas' / 'xml_data'


def get_xml_url(url2json: Dict=PATH_PRODUCTS_INFOS) -> Dict[str, List]:
    """Get JSON URL giving access to XML URL for each orphadata product

    Parameters
    ----------
    url2json : Dict, optional
        Dictionary relating product and their JSON url, by default PATH_PRODUCTS_INFOS

    Returns
    -------
    Dict
        Dictionary relating product and their XML url
    """
    logger.info('Accessing JSON files to access XML URLs...')
    xml_dict = {}

    for product, url in url2json.items():        
        logger.info('GET request to {}'.format(url))
        response = requests.get(url)
        if response.ok:
            xml_dict[product] = [ x['anUrl'] for x in response.json()]

    return xml_dict


def download_xml(urls: Union[str, Path, List], outdir: Union[str, Path]=OUTPATH):
    """Download orphadata XML product

    Parameters
    ----------
    urls : Union[str, Path, List]
        URL(s) linking the XML product
    outdir : Union[str, Path], optional
        Path to download XML files to, by default OUTPATH
    """
    logger.info('Downloading XML files...')


    os.makedirs(outdir, exist_ok=True)

    if not isinstance(urls, List):
        urls = [urls]
    
    for url in urls:
        if not isinstance(url, Path):
            filename = Path(url).name
        else:
            filename = url.name

        logger.info('GET request to {}'.format(url))
        with requests.get(url=str(url)) as response:
            response.raise_for_status()

            logger.info('Writing {} into {}'.format(filename, outdir))
            with open( outdir / filename, 'wb') as _f:
                for chunk in response.iter_content(8192):
                    _f.write(chunk)


if __name__ == '__main__':

    outdir = OUTPATH
    xml_path = get_xml_url()

    for product, urls in xml_path.items():
        download_xml(urls=urls)





