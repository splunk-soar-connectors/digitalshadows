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
# File: data_breach_username_service.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

from ..model.data_breach_username_summary import DataBreachUsernameSummary
from .ds_base_service import DSBaseService
from .ds_find_service import DSFindService


class DataBreachUsernameService(DSFindService):
    def __init__(self, ds_api_key, ds_api_secret_key, proxy=None):
        super().__init__(ds_api_key, ds_api_secret_key, proxy=proxy)

    def find_all(self, view=None):
        """
        Streams all DataBreachUsernameSummary objects retrieved from the Digital Shadows API.

        :param view: DataBreachUsernameView
        :return: DataBreachUsernameSummary
        """

        if view is None:
            view = DataBreachUsernameService.data_breach_username_view()

        return self._find_all("/api/data-breach-usernames", view, DataBreachUsernameSummary)

    def find_all_pages(self, view=None):
        """
        Streams all DataBreachUsernameSummary objects retrieved from the Digital Shadows API in page groups.

        :param view: DataBreachUsernameView
        :return: DataBreachUsernameSummary
        """

        if view is None:
            view = DataBreachUsernameService.data_breach_username_view()

        return self._find_all_pages("/api/data-breach-usernames", view, DataBreachUsernameSummary)

    @staticmethod
    @DSBaseService.sorted("username")
    @DSBaseService.paginated(offset=0, size=500)
    def data_breach_username_view(published="ALL", domain_names=None, username="*", review_statues=None):
        return {
            "filter": {
                "published": published,
                "domainNames": [] if domain_names is None else domain_names,
                "username": username,
                "reviewStatuses": [] if review_statues is None else review_statues,
            }
        }
