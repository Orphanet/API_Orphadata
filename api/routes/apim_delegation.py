from datetime import datetime
from typing import Dict, List
from flask import Blueprint, redirect, render_template, request
from pathlib import Path
from urllib.parse import urlencode

from dotenv import load_dotenv
module_path = Path(__file__).parent.parent / 'services'
load_dotenv(module_path / '.arm_env')

from ..services import arm_apiQueries
from ..services.azure_query_models import queryParams
from ..services.arm_settings import APIM_DEV_PORTAL_URL


bp = Blueprint('delegation', __name__, url_prefix='/apim-delegation')


@bp.route('/', methods=('GET', 'POST'))
def index():
    query_params = queryParams(request=request)
    if not query_params.validate_request():
        return 'Error, the source of the request is not allowed to access this page...', 401

    if query_params.operation == 'SignUp':
        return render_template('apim-signup.html', params=query_params)

    if query_params.operation == 'SignIn':
        return render_template('apim-signin.html', params=query_params)

    if query_params.operation == 'SignOut':
        return redirect(APIM_DEV_PORTAL_URL + '?' + query_params.returnUrl)

    if query_params.operation == 'Subscribe':
        product = arm_apiQueries.get_product(product_id=query_params.productId)
        return render_template('apim-subscribe.html', params=query_params, product=product)

    if query_params.operation == 'Unsubscribe':
        arm_apiQueries.update_subscription_state(sid=query_params.subscriptionId, state="cancelled")
        query_params.returnUrl = APIM_DEV_PORTAL_URL
        return render_template('apim-unsubscribe.html', params=query_params)


@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    if request.form.get('checkbox-cgu'):
        cgu_acceptance = "CGU accepted on the following date: {} (UTC)".format(datetime.utcnow().isoformat())
    else:
        cgu_acceptance = "CGU not accepted"

    note = "- Country: {}\n- Institution: {}\n- Position: {}\n- Usage purposes: {}\n- CGU acceptance: {}".format(
        request.form.get('country'),
        request.form.get('institution'),
        request.form.get('position'),
        request.form.get('usage-intention'),
        cgu_acceptance
    )

    data = {
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'firstName': request.form.get('first-name'),
        'lastName': request.form.get('last-name'),
        'note': note,
        'confirmation': "signup"
    }


    query_params = {
        'returnUrl': request.form.get('returnUrl'),
        'operation': request.form.get('operation'),
        'salt': request.form.get('salt'),
        'sig': request.form.get('sig')
    }

    response = arm_apiQueries.create_user(user_contract=data)

    if 'error' in response:
        query_params.update(errorMessage='One or more fields are invalid.')
        return redirect('/apim-delegation?' + urlencode(query_params))

    auth_response = arm_apiQueries.authenticate_user(email=data['email'], password=data['password'])
    if not auth_response['authenticated']:
        query_params.update(errorMessage='Error in authentication process.')
        return redirect('/apim-delegation?' + urlencode(query_params))

    sso_token_response = arm_apiQueries.get_shared_access_token(user_id=auth_response['userId'])
    sso_token = sso_token_response.get('value', None)

    if not sso_token:
        query_params.update(errorMessage='Error in generating SSO token.')
        return redirect('/apim-delegation?' + urlencode(query_params))

    redirect_query = {
        'token': sso_token,
        'returnUrl': request.form.get('returnUrl', '/')
    }    

    redirectUrl = APIM_DEV_PORTAL_URL + "/signin-sso?" + urlencode(redirect_query)
    return redirect(redirectUrl)


@bp.route('/signin', methods=('GET', 'POST'))
def signin():
    data = {
        'email': request.form.get('email'),
        'password': request.form.get('password'),
    }

    query_params = {
        'returnUrl': request.form.get('returnUrl'),
        'operation': request.form.get('operation'),
        'salt': request.form.get('salt'),
        'sig': request.form.get('sig')
    }

    auth_response = arm_apiQueries.authenticate_user(email=data['email'], password=data['password'])

    if not auth_response['authenticated']:
        query_params.update(errorMessage='Invalid credentials')
        return redirect('/apim-delegation?' + urlencode(query_params))

    sso_token_response = arm_apiQueries.get_shared_access_token(user_id=auth_response['userId'])
    sso_token = sso_token_response.get('value', None)

    if not sso_token:
        query_params.update(errorMessage='Error in generating SSO token.')
        return redirect('/apim-delegation?' + urlencode(query_params))

    redirect_query = {
        'token': sso_token,
        'returnUrl': request.form.get('returnUrl', '/')
    }    

    redirectUrl = APIM_DEV_PORTAL_URL + "/signin-sso?" + urlencode(redirect_query)
    return redirect(redirectUrl)


@bp.route('/subscribe', methods=('GET', 'POST'))
def subscribe():

    query_params = {
        'operation': request.form.get('operation'),
        'salt': request.form.get('salt'),
        'sig': request.form.get('sig'),
        'productId': request.form.get('productId'),
        'userId': request.form.get('userId'),
    }

    response = arm_apiQueries.create_subscription(user_id=request.form.get('userId'), product_id=request.form.get('productId'), subscription_name=request.form.get('subscriptionName'))
    
    if 'error' in response:
        query_params.update(errorMessage=response["error"]["message"])
        return redirect('/apim-delegation?' + urlencode(query_params))

    redirectUrl = APIM_DEV_PORTAL_URL + '/product#product={}'.format(request.form.get('productId'))
    return redirect(redirectUrl)
