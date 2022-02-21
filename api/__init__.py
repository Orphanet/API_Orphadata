#!/usr/bin/env python3

from pathlib import Path
import os
from flask import jsonify, request
import connexion
from dotenv import load_dotenv

from api.util import JSONEncoder

module_path = Path(__file__).parent.parent
load_dotenv(module_path / '.varenv')  # load variable environments for elasticsearch config
from .config import config_by_name


def create_app(config_name):
    options = {'swagger_url': '/'}
    app = connexion.App(__name__, specification_dir='./swagger/', options=options)
    with app.app.app_context():
        print(config_name)
        app.app.config.from_object(config_by_name[config_name])
        app.add_api('swagger_apim.yaml', arguments={'title': 'API Orphadata'}, pythonic_params=True)

    app.app.static_folder = module_path / 'static'
    app.app.json_encoder = JSONEncoder

    app.app.jinja_env.globals['workaround_for_API_contract'] = "./openapi.json"  # manual override of the API_contract url, comment to return to default. cf templates/index.j2
    app.app.jinja_env.globals["defaultModelsExpandDepth"] = "-1"  # do not display data models

    @app.route('/apim-delegation')
    def index():
        q_operation = request.args.get('operation', 'no operation found')
        return "<h1>apim delegation page</h1><p>{}</p>".format(q_operation)


    

    return app.app


if __name__ == '__main__':
    app = create_app(config_name=os.getenv('FLASK_ENV', 'test'))
    app.run()
