# import config
# import swagger_server.controllers.query_controller as qc


# es = config.elastic_server


# orphacode = 166024
# language = 'en'

# index = "product1"
# index = "{}_{}".format(language.lower(), index)


# query = {
#     "query": {
#         "match": {
#             "Preferred term": "Multiple epiphyseal dysplasia, Al-Gazali type"
#             }
#         }
#     }

# query = {
#     "query": {
#         "query_string": {
#             "query": "Multiple epiphyseal dysplasia, Al-Gazali type",
#             "default_field": "Preferred term"
#             }
#         }
#     }

# response = qc.single_res(es, index, query)
# response
# [x["ORPHAcode"] for x in response]

