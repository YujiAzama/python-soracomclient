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

from soracomclient.client import ClientBase


class Group(ClientBase):

    _path = "/groups"

    def __init__(self, auth):
        super(Group, self).__init__(auth.api_key, auth.token)

    def list_groups(self, group_id=None, **params):
        if group_id:
            return self.get("%s/%s" % (self._path, group_id))
        else:
            return self.get("%s" % self._path, params=params)

    def create_group(self, tags):
        body = {}
        if tags:
            body = {"tags": tags}
        return self.post("%s" % self._path, body=body)

    def delete_group(self, group_id):
        return self.delete("%s/%s" % (self._path, group_id))

    def get_group(self, group_id):
        return self.get("%s/%s" % (self._path, group_id))

    def list_subscribers_in_group(self, group_id, **params):
        return self.get("%s/%s/subscribers" % (self._path, group_id),
                        params=params)

    def update_group_configuration(self, group_id, namespace="SoracomAir",
                                   **params):
        return self.put("%s/%s/configuration/%s" % (self._path, group_id,
                                                    namespace),
                        body=params)

    def delete_group_configuration(self, group_id, namespace, name):
        return self.delete("%s/%s/configuration/%s/%s" % (self._path,
                                                          group_id,
                                                          namespace,
                                                          name))

    def update_group_tags(self, group_id, tags={}):
        return self.put("%s/%s/tags" % (self._path, group_id), body=tags)

    def delete_group_tags(self, group_id, name):
        return self.delete("%s/%s/tags/%s" % (self._path, group_id, name))
