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
# File: infrastructure_ssl_service.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

from ..model.infrastructure_ssl import InfrastructureSSL
from .ds_base_service import DSBaseService
from .ds_find_service import DSFindService


class InfrastructureSSLService(DSFindService):
    def __init__(self, ds_api_key, ds_api_secret_key, proxy=None):
        super().__init__(ds_api_key, ds_api_secret_key, proxy=proxy)

    def find_all(self, view=None):
        """
        Streams all infrastructure objects retrieved from the Digital Shadows API.

        :param view: InfrastructureView
        :return: Infrastructure generator
        """

        if view is None:
            view = InfrastructureSSLService.infrastructure_ssl_view()

        return self._find_all("/api/secure-socket", view, InfrastructureSSL)

    def find_all_pages(self, view=None):
        """
        Streams all infrastructure objects retrieved from the Digital Shadows API in page groups.

        :param view: InfrastructureView
        :return: Infrastructure generator
        """

        if view is None:
            view = InfrastructureSSLService.infrastructure_ssl_view()

        return self._find_all_pages("/api/secure-socket", view, InfrastructureSSL)

    @staticmethod
    @DSBaseService.paginated(size=500)
    @DSBaseService.sorted("published")
    def infrastructure_ssl_view(
        published="ALL",
        domain=None,
        detected="ALL",
        grades=None,
        markedclosed=False,
        determinedresolved=False,
        issues=None,
        statuses=None,
        revoked=False,
        incidenttypes=None,
        severities=None,
        alerted=False,
        reverse=None,
    ):
        view = {
            "filter": {
                "published": published,
                "detected": detected,
                "grades": [] if grades is None else grades,
                "incidentTypes": [] if incidenttypes is None else incidenttypes,
                "severities": [] if severities is None else severities,
                "statuses": [] if statuses is None else statuses,
                "alerted": "true" if alerted else "false",
                "revoked": "true" if revoked else "false",
                "markedClosed": "true" if markedclosed else "false",
                "determinedResolved": "true" if determinedresolved else "false",
            }
        }
        if domain is not None:
            view["filter"]["domain"] = domain

        if reverse is not None:
            view["sort"] = {"direction": "ASCENDING" if reverse else "DESCENDING", "property": "published"}

        return view
