# Copyright 2016 Yuji Azama
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

import json
import requests


ENDPOINT_URL = 'https://api.soracom.io'
API_VERSION = '/v1'
API_BASE_URL = ENDPOINT_URL + API_VERSION

class HTTPClient(object):
    
    def do_request(self, url, method, body=None, headers=None, **kwargs):
        resp = requests.request(method, ENDPOINT_URL + API_VERSION + url,
                                data=body, headers=headers, **kwargs)
        return resp, resp.text


class ClientBase(object):

    def __init__(self, api_key, token, **kwargs):
        super(ClientBase, self).__init__()
        self.headers = self._create_header(api_key, token)
        self.httpclient = construct_http_client(**kwargs)
        self.retries = kwargs.pop('retries', 0)

    def _create_header(self, api_key, token):
        headers = {'Content-Type': 'application/json'}
        if api_key:
            headers['X-Soracom-Api-Key'] = api_key
        if token:
            headers['X-Soracom-Token'] = token
        return headers

    def _parse_response(self, status, reply_body):
        if reply_body == "":
            reply_body = json.loads(reply_body)
        return status, reply_body

    def do_request(self, method, action, body=None, headers=None, params=None):
        status, reply_body = self.httpclient.do_request(action, method,
                                              body=json.dumps(body),
                                              headers=self.headers,
                                              params=params)
        return self._parse_response(status, reply_body)

    def retry_request(self, method, action, body=None, headers=None,
                      params=None):
        max_attempts = self.retries + 1
        for i in range(max_attempts):
            return self.do_request(method, action, body=body, headers=headers,
                                   params=params)

    def get(self, action, body=None, headers=None, params=None):
        return self.retry_request("GET", action, body=body, headers=headers,
                                  params=params)

    def post(self, action, body=None, headers=None, params=None):
        return self.do_request("POST", action, body=body, headers=headers,
                               params=params)

    def put(self, action, body=None, headers=None, params=None):
        return self.retry_request("PUT", action, body=body, headers=headers,
                                  params=params)

    def delete(self, action, body=None, headers=None, params=None):
        return self.retry_request("DELETE", action, body=body, headers=headers,
                                  params=params)


def construct_http_client(**kwargs):
    return HTTPClient(**kwargs)
