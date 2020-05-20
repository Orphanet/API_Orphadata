from elasticsearch import Elasticsearch

elastic_server = Elasticsearch(hosts=["localhost"])
scroll_timeout = "2m"
