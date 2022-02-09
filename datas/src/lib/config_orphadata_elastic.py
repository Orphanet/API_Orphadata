import pathlib
import elasticsearch


# elastic_node = elasticsearch.Elasticsearch(hosts=["localhost"], timeout=30, max_retries=3, retry_on_timeout=True)  #  load elastic node
elastic_node = elasticsearch.Elasticsearch(
                ['https://9d2d8c7975624d95aa964a1d22a96daf.eu-west-1.aws.found.io'],
                port=9243,
                http_auth=('elastic', 'fSowAPgpKjaA3hD6T7NxctEf'),
                timeout=180, max_retries=3, retry_on_timeout=True
)
