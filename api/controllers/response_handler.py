from typing import Dict, Tuple, Union, List

from flask.wrappers import Request
from flask import request


class ResponseWrapper:

    def __init__(self, ctl_response: Union[List, Dict, Tuple], request: Request, product: Dict):
        self.ctl_response = ctl_response
        self.request = request
        self.product = product
        self.wrapper = self.valid_wrapper() if not isinstance(ctl_response, tuple) else self.error_wrapper()
        self.status_code = 200 if self.wrapper == self.valid_wrapper() else None
        self._ready = False

    def valid_wrapper(self):
        return {
            'uri': '',
            'parameters': {
                'path': {},
                'query': {}
            },
            'datasetCategory': {
                # 'ID': '',
                'name': '',
                'lang': '',
            },
            'data': {
                '__licence': {
                    "name": "Creative Commons Attribution 4.0 International",
                    "identifier": "CC-BY-4.0",
                    "link": "https://creativecommons.org/licenses/by/4.0"
                },
                '__count': None,
                'results': None
            }
        }

    def error_wrapper(self):
        return {
            'error': {
                'code': None,
                'type': '',
                'message': '',
            }
        }

    def get(self) -> Tuple[Dict, int]:
        if not self._ready:
            if not self.wrapper.get('error'):
                self.wrapper['uri'] = self.request.full_path if self.request.args else self.request.path
                self.wrapper['datasetCategory'] = self.product
                self.wrapper['data']['results'] = self.ctl_response
                self.wrapper['data']['__count'] = len(self.ctl_response) if isinstance(self.ctl_response, list) else 1
                if hasattr(self.request.args, 'params'):
                    for k, v in request.args.params.items():
                        self.wrapper['parameters']['path'][k] = v
                if request.args:
                    for k, v in request.args.items():
                        self.wrapper['parameters']['query'][k] = v
            else:
                self.wrapper['error']['code'] = self.ctl_response[1]
                self.wrapper['error']['type'] = self.ctl_response[0]
                self.wrapper['error']['message'] = 'message to define'

            self._ready = True

        return self.wrapper, self.status_code or self.wrapper['error']['code']