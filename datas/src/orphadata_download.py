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
import time
from tqdm import tqdm

from lib.config import ROOT_DIR, PATH_PRODUCTS_INFOS


FORMAT = '%(asctime)-26s %(name)-26s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
name = __name__ if __name__ != '__main__' else 'orphadata_download'
logger = logging.getLogger(name)

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
            xml_dict[product] = [ x['anUrl'] for x in response.json() if 'product3_235' not in x['anUrl'] ]

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
    _notqdm = True if __name__ == '__main__' else False

    os.makedirs(outdir, exist_ok=True)

    if not isinstance(urls, List):
        urls = [urls]
    
    for url in tqdm(iterable=urls, desc='Downloaded XML files', total=len(urls), disable=_notqdm, ncols=100, colour='blue'):
        if not isinstance(url, Path):
            filename = Path(url).name
        else:
            filename = url.name

        logger.info('GET request to {}'.format(url))
        with requests.get(url=str(url)) as response:
            response.raise_for_status()

            logger.info('Writing {} into {}'.format(filename, outdir))
            with open( outdir / filename, 'wb') as _f:
                for chunk in response.iter_content(50*1024*1024):
                    _f.write(chunk)


def main():
    xml_path = get_xml_url()
    _notqdm = True if __name__ == '__main__' else False

    for _, urls in tqdm(iterable=xml_path.items(), desc="Processed products", total=len(xml_path.values()), ncols=150, disable=_notqdm):
        download_xml(urls=urls)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    logger.info('Download process has finished. Time: {:.2f}'.format(end_time-start_time))