from elasticsearch import Elasticsearch

# ELASTIC SEARCH
# Local test
elastic_server = Elasticsearch(hosts=["localhost"])

# Local test from docker
# elastic_server = Elasticsearch(hosts=["host.docker.internal"])

# Online
# Check redmine ticket http://redminor.orpha.net/issues/
# ES endpoint
# es_url = "https://"
# es_api_key = {"id": "",
#               "name": "",
#               "api_key": ""
#               }
# elastic_server = Elasticsearch(hosts=[es_url], api_key=(es_api_key["id"], es_api_key["api_key"]))


scroll_timeout = "2m"
