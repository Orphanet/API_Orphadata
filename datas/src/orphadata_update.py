import logging
import time

from lib import utils
FORMAT = '%(asctime)-26s %(name)-26s %(message)s'
utils.addLoggingLevel('BASIC_LOG', 55, methodName='basic_log')
logging.basicConfig(format=FORMAT, level=logging.BASIC_LOG)
logger = logging.getLogger('orphadata_update')


import orphadata_download
import orphadata_xml2json
import orphadata_injection


def main():
    
    logger.basic_log("Update process - step 1: starting download of data...")
    orphadata_download.main()
    logger.basic_log("Update process - step 1: download completed")
    logger.basic_log("")

    logger.basic_log("Update process - step 2: starting conversion of XML data to elastic compatible JSON")
    orphadata_xml2json.main()
    logger.basic_log("Update process - step 2: conversion completed")
    logger.basic_log("")

    logger.basic_log("Update process - step 3: starting elastic injection of JSON data...")
    json_filenames = orphadata_injection.get_jsons(path=orphadata_injection.PATH2JSON)
    es_client = orphadata_injection.esConnector(url='local')
    orphadata_injection.main(es_client=es_client, json_path=json_filenames)
    logger.basic_log("Update process - step 3: injection completed")
    logger.basic_log("")




if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    logger.basic_log('Update process has finished. Time: {:.2f}'.format(end_time-start_time))