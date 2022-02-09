#!/usr/bin/env python3

from pathlib import Path
import os

import connexion
from dotenv import load_dotenv
from flask import current_app, send_from_directory, send_file

from api.util import JSONEncoder

module_path = Path(__file__).parent.parent
load_dotenv(module_path / '.varenv')  # load variable environments for elasticsearch config
from .config import config_by_name


def create_app(config_name):
    options = {'swagger_url': '/'}
    app = connexion.App(__name__, specification_dir='./swagger/', options=options)
    with app.app.app_context():
        app.app.config.from_object(config_by_name[config_name])
        app.add_api('swagger.yaml', arguments={'title': 'API Orphadata'}, pythonic_params=True)

    app.app.static_folder = module_path / 'static'
    app.app.json_encoder = JSONEncoder

    app.app.jinja_env.globals['workaround_for_API_contract'] = "./openapi.json"  # manual override of the API_contract url, comment to return to default. cf templates/index.j2
    app.app.jinja_env.globals["defaultModelsExpandDepth"] = "-1"  # do not display data models

    return app.app


if __name__ == '__main__':
    app = create_app(config_name=os.getenv('FLASK_ENV', 'test'))
    app.run()
