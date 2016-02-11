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
                 token=None, timeout=None):
        super(Auth, self).__init__(api_key, token)
        self._email = email
        self._password = password
        if api_key is None:
            self._api_key, self._operator_id, self._token = self.auth(email,
                                                                      password,
                                                                      timeout)
        else:
            self._api_key = api_key
            self._operator_id = operator_id
            self._token = token

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def api_key(self):
        return self._api_key

    @property
    def operator_id(self):
        return self._operator_id

    @property
    def token(self):
        return self._token

    def auth(self, email, password, timeout):
        body = {"email": email,
                "password": password}
        if timeout:
            body["tokenTimeoutSeconds"] = timeout
        response, body = self.post(self.path, body=body)
        #body = json.loads(body)
        return body['apiKey'], body['operatorId'], body['token']
