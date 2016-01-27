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


class Subscriber(ClientBase):

    _path = "/subscribers"

    def __init__(self, auth):
        super(Subscriber, self).__init__(auth.api_key, auth.token)

    def list_subscribers(self, **params):
        return self.get("%s" % self._path, params=params)

    def register(self, imsi, registration_secret, group_id=None, tags={}):
        body = {"registration_secret": registration_secret,
                "tags": tags}
        if group_id:
            body['group_id'] = group_id

        return self.post("%s/%s/register" % (self._path, imsi), body=body)

    def get_subscriber(self, imsi):
        return self.get("%s/%s" % (self._path, imsi))

    def update_subscriber_speed_class(self, imsi, speed_class):
        body = {"speedClass": speed_class}
        return self.post("%s/%s/update_speed_class" % (self._path, imsi),
                         body=body)

    def activate_subscriber(self, imsi):
        return self.post("%s/%s/activate" % (self._path, imsi))

    def deactivate_subscriber(self, imsi):
        return self.post("%s/%s/deactivate" % (self._path, imsi))

    def terminate_subscriber(self, imsi):
        return self.post("%s/%s/terminate" % (self._path, imsi))

    def enable_termination(self, imsi):
        return self.post("%s/%s/enable_termination" % (self._path, imsi))

    def disable_termination(self, imsi):
        return self.post("%s/%s/disable_termination" % (self._path, imsi))

    def set_expiry_time(self, imsi, expiry_time):
        body = {"expiryTime": expiry_time}
        return self.post("%s/%s/set_expiry_time" % (self._path, imsi),
                         body=body)

    def unset_expiry_time(self, imsi):
        return self.post("%s/%s/unset_expiry_time" % (self._path, imsi))

    def set_group(self, imsi, group_id):
        body = {"groupId": group_id}
        return self.post("%s/%s/set_group" % (self._path, imsi), body=body)

    def unset_group(self, imsi):
        return self.post("%s/%s/unset_group" % (self._path, imsi))

    def update_subscriber_tags(self, imsi, tags):
        return self.put("%s/%s/tags" % (self._path, imsi), body=tags)

    def delete_subscriber_tag(self, imsi, tag_name):
        return self.delete("%s/%s/tags/%s" % (self._path. imsi, tag_name))
