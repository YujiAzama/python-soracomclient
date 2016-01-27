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


class Operator(ClientBase):

    _path = "/operators"

    def __init__(self, auth):
        super(Operator, self).__init__(auth.api_key, auth.token)
        self._auth = auth

    def generate_new_token(self, seconds):
        body = {"tokenTimeoutSeconds": seconds}

        return self.post("%s/%s/token" % (self._path, self._auth.operator_id),
                         body=body)

    def update_password(self, current_passwd, new_passwd):
        body = {"currentPassword": current_passwd,
                "newPassword": new_passwd}

        return self.post("%s/%s/password" % (self._path,
                                             self._auth.operator_id),
                         body=body)

    def generate_token_for_support_console(self):
        return self.post("%s/%s/support/token" % (self._path,
                                                  self._auth.operator_id))

    def create(self, email, password):
        """ Create Operator """
        body = {"email": email, "password": password}

        return self.post(self._path, body=body)

    def verify(self, token):
        """ Verify Operator """
        body = {"token": token}

        return self.post("%s/verify" % self._path, body=body)

    def get_operator(self):
        """ Get Operator """
        return self.get("%s/%s" % (self._path, self._auth.operator_id))
