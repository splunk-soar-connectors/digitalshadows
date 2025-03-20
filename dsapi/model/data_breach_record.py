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
# File: data_breach_record.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

from .ds_model import DSModel


class DataBreachRecord(DSModel):
    def __init__(
        self,
        record_id,
        username,
        password,
        review,
        published,
        prior_username_breach_count,
        prior_username_password_breach_count,
        prior_row_text_breach_count,
        payload,
    ):
        self._id = record_id
        self._username = username
        self._password = password
        self._review = review
        self._published = published
        self._prior_username_breach_count = prior_username_breach_count
        self._prior_username_password_breach_count = prior_username_password_breach_count
        self._prior_row_text_breach_count = prior_row_text_breach_count
        self._payload = payload

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def review(self):
        return self._review

    @property
    def published(self):
        return self._published

    @property
    def prior_username_breach_count(self):
        return self._prior_username_breach_count

    @property
    def prior_username_password_breach_count(self):
        return self._prior_username_password_breach_count

    @property
    def prior_row_text_breach_count(self):
        return self._prior_row_text_breach_count

    @property
    def payload(self):
        return self._payload

    def __str__(self):
        return f"DataBreachRecord[id={self.id}, username={self.username}, payload={self.payload}]"

    @classmethod
    def from_json(cls, json):
        cast = DSModel.cast
        return cls(
            cast(json.get("id"), int),
            json.get("username"),
            json.get("password"),
            json.get("review"),
            json.get("published"),
            cast(json.get("priorUsernameBreachCount"), int),
            cast(json.get("priorUsernamePasswordBreachCount"), int),
            cast(json.get("priorRowTextBreachCount"), int),
            json,
        )
