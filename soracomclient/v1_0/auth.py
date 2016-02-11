# Copyright 2016 Yuji Azama
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json

from soracomclient.client import ClientBase


class Auth(ClientBase):

    path = "/auth"

    def __init__(self, email, password, api_key=None, operator_id=None,
                 token=None, timeout=86400):
        super(Auth, self).__init__(api_key, token)
        self._auth = {'email': email,
                      'password': password,
                      'timeout': timeout}
        if api_key is None:
            self._auth = self.auth(self._auth)
        else:
            self._auth['apiKey'] = api_key
            self._auth['operatorId'] = operator_id
            self._auth['token'] = token

    @property
    def email(self):
        return self._auth['email']

    @property
    def password(self):
        return self._auth['password']

    @property
    def api_key(self):
        return self._auth['apiKey']

    @property
    def operator_id(self):
        return self._auth['operatorId']

    @property
    def token(self):
        return self._auth['token']

    def auth(self, auth):
        body = {'email': auth['email'],
                'password': auth['password'],
                'tokenTimeoutSeconds': auth['timeout']}
        status, response = self.post(self.path, body=body)
        auth.update(response)
        return auth
