#!/usr/bin/env python3

from pathlib import Path
import os
from flask import jsonify
from flask_cors import CORS
import connexion
from dotenv import load_dotenv

# import api.routes as routes
from api.util import JSONEncoder

module_path = Path(__file__).parent.parent
load_dotenv(module_path / '.varenv')  # load variable environments for elasticsearch config
from api.config import config_by_name


def create_app(config_name):
    options = {'swagger_url': '/'}
    app = connexion.App(__name__, specification_dir='./swagger/', options=options)
    with app.app.app_context():
        app.app.config.from_object(config_by_name[config_name])
        app.add_api('swagger.yaml', arguments={'title': 'API Orphadata'}, pythonic_params=True)
    
    print(app.app.config["ES_URL"])

    app.app.static_folder = module_path / 'static'
    # app.app.template_folder = module_path / 'static'
    app.app.json_encoder = JSONEncoder

    app.app.jinja_env.globals['workaround_for_API_contract'] = "./openapi.json"  # manual override of the API_contract url, comment to return to default. cf templates/index.j2
    app.app.jinja_env.globals["defaultModelsExpandDepth"] = "-1"  # do not display data models

    from .routes import apim_delegation
    app.app.register_blueprint(apim_delegation.bp)

    from .routes import mappor
    app.app.register_blueprint(mappor.bp)

    @app.route('/list-templates')
    def list_templates():
        jinja_templates =  app.app.jinja_env.list_templates()
        return jsonify(jinja_templates)

    CORS(app.app)

    return app.app


if __name__ == '__main__':
    app = create_app(config_name=os.getenv('FLASK_ENV', 'test'))
    app.run()
