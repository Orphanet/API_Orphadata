from flask import (
    Blueprint, render_template, request
)

import api.services


bp = Blueprint('delegation', __name__, url_prefix='/apim-delegation')


@bp.route('/', methods=('GET', 'POST'))
def index():
    apim_params = {
        'referer': request.headers.get('Referer', 'refererNotFound'),
        'operation': request.args.get('operation', 'no operation found'),
        'returnUrl': request.args.get('returnUrl', 'https://orphanetapi.developer.azure-api.net/'),
        'salt': request.args.get('salt', 'no salt found'),
        'sig': request.args.get('sig', 'no sig found'),
        'userId': request.args.get('userId', 'no userId found'),
        'productId': request.args.get('productId', 'no productId found'),
        'subscriptionId': request.args.get('subscriptionId', 'no subscriptionId found'),
    }

    # template = app.app.jinja_env.get_template("apim-delegation.html")
    # return template.render(params=apim_params)

    return render_template("apim-delegation.html", params=apim_params)
