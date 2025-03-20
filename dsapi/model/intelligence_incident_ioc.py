# Copyright (c) 2025 Splunk Inc.
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
# File: intelligence_incident_ioc.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

from .ds_model import DSModel


class IntelligenceIncidentIoc(DSModel):
    def __init__(self, payload):
        self._payload = payload

    @property
    def payload(self):
        return self._payload

    def __str__(self):
        return f"IntelligenceIncidentIoc[payload={self.payload}]"

    @classmethod
    def from_json(cls, json):
        return cls(json)
