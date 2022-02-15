import logging
import os
from pathlib import Path
import time

from lib import utils, log_handler

BASE_PATH = Path(__file__).resolve().parent.parent
LOG_PATH = BASE_PATH / 'logs/update_data.log'

logger_name = 'orphadata_update' if __name__ == '__main__' else __name__
logger = log_handler.Logger(name=logger_name, outpath=LOG_PATH)


# FORMAT = '%(asctime)-26s %(name)-26s %(message)s'
# utils.addLoggingLevel('BASIC_LOG', 55, methodName='basic_log')
# logging.basicConfig(format=FORMAT, level=logging.BASIC_LOG)
# logger = logging.getLogger('orphadata_update')


import orphadata_download
import orphadata_xml2json
import orphadata_injection

DATA_ENV = os.getenv('DATA_ENV', 'remote')

def main():
    url = 'remote' if DATA_ENV == 'remote' else 'local'
    
    logger.basic_log("Update process - step 1: starting download of data...".upper())
    orphadata_download.main()
    logger.basic_log("Update process - step 1: download completed".upper())
    logger.basic_log("")

    logger.basic_log("Update process - step 2: starting conversion of XML data to elastic compatible JSON".upper())
    orphadata_xml2json.main()
    logger.basic_log("Update process - step 2: conversion completed".upper())
    logger.basic_log("")

    logger.basic_log("Update process - step 3: starting injection of JSON data on {} elastic instance...".format(url).upper())
    json_filenames = orphadata_injection.get_jsons(path=orphadata_injection.PATH2JSON)
    es_client = orphadata_injection.esConnector(url=url)
    orphadata_injection.main(es_client=es_client, json_path=json_filenames)
    logger.basic_log("Update process - step 3: injection completed".upper())
    logger.basic_log("")


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    logger.basic_log('Update process has finished. Time: {:.2f}'.format(end_time-start_time))

