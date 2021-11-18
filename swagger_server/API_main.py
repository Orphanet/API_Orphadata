#!/usr/bin/env python3

import os

import connexion
from flask import send_from_directory, send_file
# from livereload import Server

from swagger_server import encoder
# import werkzeug
# werkzeug.cached_property = werkzeug.utils.cached_property

def main():
    # swagger_url => path to ui
    options = {'swagger_url': '/'}
    app = connexion.App(__name__, specification_dir='./swagger/', options=options)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API Orphadata'}, pythonic_params=True)

    # manual override of the API_contract url, comment to return to default. cf templates/index.j2
    app.app.jinja_env.globals['workaround_for_API_contract'] = "./openapi.json"

    # defaultModelsExpandDepth = -1 => do not display data models
    app.app.jinja_env.globals["defaultModelsExpandDepth"] = "-1"

    # Workaround to serve media in development server
    # Comment for production
    @app.route("/media/<image>")
    def media_for_dev(image):
        return send_from_directory("../media/", image)


    @app.route('/my-styles.css')
    def custom_css_theme():
        return send_file('../media/css/theme-newspaper.css')

    # Force the direct encoding of accents in json
    # app.app.config['JSON_AS_ASCII'] = False

    # Remove A-z sorting in json
    # app.app.config['JSON_SORT_KEYS'] = False
    application = app.app
    application.run(port=8080, debug=True, extra_files=['./swagger_server/swagger/swagger.yaml'])


if __name__ == '__main__':
    app = main()
    # server = Server(app.wsgi_app)
    # server.serve()
    app.run(port=8080, debug=True, extra_files=['./swagger_server/swagger/swagger.yaml'])
