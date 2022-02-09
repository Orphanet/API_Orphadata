from flask import current_app

PRODUCTS = current_app.config.get('PRODUCTS')
es_client = current_app.config.get('ES_NODE')
