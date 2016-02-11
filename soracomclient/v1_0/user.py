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


class User(ClientBase):

    path = "/operators/%s/users"

    def __init__(self, auth):
        super(User, self).__init__(auth.api_key, auth.token)
        self.auth = auth
        self.path = self.path % auth.operator_id

    def list_users(self):
        return self.get(self.path)

    def delete_user(self, username):
        return self.delete("%s/%s" % (self.path, username))

    def get_user(self, username):
        return self.get("%s/%s" % (self.path, username))

    def create_user(self, username, description=""):
        body = {"description": description}
        return self.post("%s/%s" % (self.path, username), body=body)

    def update_user(self, username, description=""):
        body = {"description": description}
        return self.put("%s/%s" % (self.path, username), body=body)

    def list_user_auth_keys(self, username):
        return self.get("%s/%s/auth_keys" % (self.path, username))

    def generate_user_auth_key(self, username):
        return self.post("%s/%s/auth_keys" % (self.path, username))

    def delete_user_auth_key(self, username, auth_key_id):
        return self.delete("%s/%s/auth_keys/%s" % (self.path,
                                                   username,
                                                   auth_key_id))

    def get_user_auth_key(self, username, auth_key_id):
        return self.get("%s/%s/auth_keys/%s" % (self.path, username,
                                                auth_key_id))

    def delete_user_password(self, username):
        return self.delete("%s/%s/password" % (self.path, username))

    def has_user_password(self, username):
        return self.get("%s/%s/password" % (self.path, username))

    def create_user_password(self, username, password):
        body = {"password": password}
        return self.post("%s/%s/password" % (self.path, username), body=body)

    def get_user_permission(self, username):
        return self.get("%s/%s/permission" % (self.path, username))

    def update_user_permission(self, username, permission="", description=""):
        body = {"permission": permission,
                "description": description}
        return self.put("%s/%s/permission" % (self.path, username), body=body)
