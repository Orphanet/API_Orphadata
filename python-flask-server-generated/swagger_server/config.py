from elasticsearch import Elasticsearch

# elastic_server = Elasticsearch(hosts=["localhost"])
elastic_server = Elasticsearch(hosts=["host.docker.internal"])
scroll_timeout = "2m"
