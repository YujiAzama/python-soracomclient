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


class EventHandler(ClientBase):

    _path = "/event_handlers"

    def __init__(self, auth):
        super(EventHandler, self).__init__(auth.api_key, auth.token)

    def list_event_handlers(self, handler_id=None, target=None, imsi=None):
        if handler_id:
            return self.get("%s/%s" % (self._path, handler_id))
        elif target:
            return self.get("%s" % self._path, params={"target": target})
        elif imsi:
            return self.get("%s/subscribers/%s" % (self._path, imsi))
        else:
            return self.get("%s" % self._path)

    def create_event_handler(self, req):
        return self.post("%s" % self._path, body=req)

    def get_event_handler(self, handler_id):
        return self.get("%s/%s" % (self._path, handler_id))

    def delete_event_handler(self, handler_id):
        return self.delete("%s/%s" % (self._path, handler_id))

    def update_event_handler(self, handler_id, req):
        return self.put("%s/%s" % (self._path, handler_id), body=req)
