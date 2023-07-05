from typing import List
from connexion.exceptions import OAuthProblem
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

TOKEN_DB = {
    'test': {
        'uid': 100
    }
}

ADMIN_TOKEN_DB = {
    'admin': {
        'uid': "admin"
    }
}


def check_AdminSecurity(api_key, required_scopes):
    info = ADMIN_TOKEN_DB.get(api_key, None)
    if not info:
        raise OAuthProblem('Invalid token')
    return {'test_key': info}


# def check_UserSecurity(api_key, required_scopes):
#     """
#     user key must be in TOKEN_DB
#     """
#     info = TOKEN_DB.get(api_key, None)
#     if not info:
#         raise OAuthProblem('Invalid token')
#     return info


def check_UserSecurity(api_key, required_scopes):
    """
    Unlocked user version
    """
    return {'test_key': 'test'}
