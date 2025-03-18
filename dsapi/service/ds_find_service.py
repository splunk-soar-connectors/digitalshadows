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
# File: ds_find_service.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

from ..model.ds_pagination_grouping_iterator import DSPaginationGroupingIterator
from ..model.ds_pagination_iterator import DSPaginationIterator
from .ds_base_service import DSBaseService


class DSFindService(DSBaseService):
    """
    Generic Service that implements find_all and find_all_pages for Digital Shadows API objects.
    """

    def __init__(self, ds_api_key, ds_api_secret_key, proxy=None):
        super().__init__(ds_api_key, ds_api_secret_key, proxy=proxy)

    def _find_all(self, endpoint, view, cls):
        """
        Streams all DSModel objects retrieved from the Digital Shadows API.

        :type endpoint: str
        :type view: dict
        :type cls: DSModel
        :param endpoint: Digital Shadows API endpoint eg. /api/data-breach
        :param view: Digital Shadows endpoint View
        :param cls: DSModel class to be instantiated
        :return: DSModel
        """

        path = f"{endpoint}/find"
        provider = self._scrolling_request(path, method="POST", body=view)
        return DSPaginationIterator(provider, cls)

    def _find_all_pages(self, endpoint, view, cls):
        """
        Streams all DSModel objects retrieved from the Digital Shadows API in page groups.

        :type endpoint: str
        :type view: dict
        :type cls: DSModel
        :param endpoint: Digital Shadows API endpoint eg. /api/data-breach
        :param view: Digital Shadows endpoint View
        :param cls: DSModel class to be instantiated
        :return: DSModel
        """

        path = f"{endpoint}/find"
        provider = self._scrolling_request(path, method="POST", body=view)
        return DSPaginationGroupingIterator(provider, cls)

    def _read_all_pages(self, endpoint, view, cls):
        """
        Streams all DSModel objects retrieved from the Digital Shadows API in page groups.

        :type endpoint: str
        :type view: dict
        :type cls: DSModel
        :param endpoint: Digital Shadows API endpoint eg. /api/data-breach
        :param view: Digital Shadows endpoint View
        :param cls: DSModel class to be instantiated
        :return: DSModel
        """

        path = f"{endpoint}"
        provider = self._scrolling_request(path, method="POST", body=view)
        return DSPaginationGroupingIterator(provider, cls)
