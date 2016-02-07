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

from soracomclient.client import ClientBase


class Credential(ClientBase):

    _path = "/credentials"

    def __init__(self, auth):
        super(Credential, self).__init__(auth.api_key, auth.token)

    def list_credentials(self):
        return self.get("%s" % self._path)

    def create_credential(self, credentials_id, credentials):
        return self.post("%s/%s" % (self._path, credentials_id),
                         body=credentials)

    def delete_credential(self, credentials_id):
        return self.delete("%s/%s" % (self._path, credentials_id))
