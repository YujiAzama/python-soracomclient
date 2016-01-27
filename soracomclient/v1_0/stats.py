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


class Stats(ClientBase):

    _path = "/stats"

    def __init__(self, auth):
        super(Stats, self).__init__(auth.api_key, auth.token)
        self._auth = auth

    def get_air_usage(self, imsi, from_unixtime=None, to_unixtime=None,
                      period="minutes"):
        params = {"from": from_unixtime,
                  "to": to_unixtime,
                  "period": period}
        return self.get("%s/air/subscribers/%s" % (self._path, imsi),
                        params=params)

    def get_beam_usage(self, imsi, from_unixtime=0, to_unixtime=0,
                       period="minutes"):
        params = {"from": from_unixtime,
                  "to": to_unixtime,
                  "period": period}
        return self.get("%s/beam/subscribers/%s" % (self._path, imsi),
                        params=params)

    def export_air_usage(self, operator_id=None,
                         from_unixtime=0, to_unixtime=0, period="day"):
        if operator_id == None:
            operator_id = self._auth.operator_id
        body = {"from": from_unixtime,
                "to": to_unixtime,
                "period": period}
        return self.post("%s/air/operators/%s/export" % (self._path,
                                                         operator_id),
                         body=body)

    def export_beam_usage(self, operator_id=None,
                          from_unixtime=0, to_unixtime=0, period="day"):
        if operator_id == None:
            operator_id = self._auth.operator_id
        body = {"from": from_unixtime,
                "to": to_unixtime,
                "period": period}
        return self.post("%s/beam/operators/%s/export" % (self._path,
                                                          operator_id),
                         body=body)
