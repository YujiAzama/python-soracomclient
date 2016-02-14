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


class Role(ClientBase):

    path = "/operators/%s"

    def __init__(self, auth):
        super(Role, self).__init__(auth.api_key, auth.token)
        self._auth = auth
        self.path = self.path % auth.operator_id

    def list_roles(self):
        return self.get("%s/roles" % self.path)

    def delete_role(self, role_id):
        return self.delete("%s/roles/%s" % (self.path, role_id))

    def get_role(self, role_id):
        return self.get("%s/roles/%s" % (self.path, role_id))

    def create_role(self, role_id, permission, description=""):
        body = {"description": description,
                "permission": permission}
        return self.post("%s/roles/%s" % (self.path, role_id), body=body)

    def update_role(self, role_id, permission, description=""):
        body = {"description": description,
                "permission": permission}
        return self.put("%s/roles/%s" % (self.path, role_id), body=body)

    def list_role_attached_users(self, role_id):
        return self.get("%s/roles/%s/users" % (self.path, role_id))

    def list_user_roles(self, username):
        return self.get("%s/users/%s/roles" % (self.path, username))

    def attach_role_to_user(self, username, role_id):
        return self.post("%s/users/%s/roles" % (self.path, username),
                         body={"roleId": role_id})

    def detach_role_from_user(self, username, role_id):
        return self.delete("%s/users/%s/roles/%s" % (self.path, username,
                                                     role_id))
