#!/usr/bin/env python3

from pathlib import Path
import os
from flask import jsonify, render_template, request
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
        apim_params = {
            'operation': request.args.get('operation', 'no operation found'),
            'returnUrl': request.args.get('returnUrl', 'https://orphanetapi.developer.azure-api.net/'),
            'salt': request.args.get('salt', 'no salt found'),
            'sig': request.args.get('sig', 'no sig found'),
        }
        template_file = 'apim-delegation.html' if config_name == 'test' else '/static/templates/apim-delegation.html'
        return render_template(template_file, params=apim_params)

    return app.app


if __name__ == '__main__':
    app = create_app(config_name=os.getenv('FLASK_ENV', 'test'))
    app.run()
