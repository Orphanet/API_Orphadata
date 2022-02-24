from typing import Dict, List
from flask import (
    Blueprint, render_template, request
)

import api.services
from ..services.azure_query_models import queryParams


bp = Blueprint('delegation', __name__, url_prefix='/apim-delegation')


@bp.route('/', methods=('GET', 'POST'))
def index():
    query_params = queryParams(request=request)
    # if not query_params.validate_request():
    #     return 'Error, it looks like the request does not come from Azure, sorry...', 401

    if query_params.operation == 'SignUp':
        return render_template('apim-signup.html', params=query_params)
    if query_params.operation == 'SignIn':
        return render_template('apim-signin.html')
    if query_params.operation == 'SignOut':
        return render_template('apim-signout.html')
    if query_params.operation == 'Subscribe':
        return render_template('apim-subscribe.html')
    if query_params.operation == 'Unsubscribe':
        return render_template('apim-unsubscribe.html')
