#!/usr/bin/env python3

import os

import connexion
from flask import send_from_directory

from swagger_server import encoder


def main():
    # swagger_url => path to ui
    options = {'swagger_url': '/'}
    app = connexion.App(__name__, specification_dir='swagger/', options=options)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API Orphadata'}, pythonic_params=True)

    # manual override of the API_contract url, comment to return to default. cf templates/index.j2
    app.app.jinja_env.globals['workaround_for_API_contract'] = "./openapi.json"

    # defaultModelsExpandDepth = -1 => do not display data models
    app.app.jinja_env.globals["defaultModelsExpandDepth"] = "-1"

    @app.route('/Orphadata-local/favicon.ico')
    def favicon_rdcode():
        return send_from_directory(os.path.join(app.root_path),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    # Force the direct encoding of accents in json
    # app.app.config['JSON_AS_ASCII'] = False

    # Remove A-z sorting in json
    # app.app.config['JSON_SORT_KEYS'] = False
    return app


if __name__ == '__main__':
    app = main()
    app.run(port=8080)
