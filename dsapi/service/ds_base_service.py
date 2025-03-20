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
# File: ds_base_service.py
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#

import base64
import json
import time
from functools import wraps

from ..config.config import ds_api_base, ds_api_host
from .ds_abstract_service import DSAbstractService


class DSBaseService(DSAbstractService):
    """
    Base Service that implements common operations for all DS services.
    """

    def __init__(self, ds_api_key, ds_api_secret_key, proxy=None):
        super().__init__(proxy=proxy)
        data_string = str(ds_api_key) + ":" + str(ds_api_secret_key)
        data_bytes = data_string.encode("ascii")
        data_bytes = base64.b64encode(data_bytes)
        self._hash = data_bytes.decode("ascii")
        self._url_base = f"{ds_api_host}{ds_api_base}"

    def _headers(self, with_content_type=True):
        headers = {
            "Authorization": f"Basic {self._hash}",
        }
        if with_content_type:
            headers["Content-Type"] = "application/json"

        return headers

    def _request(self, path, method="GET", body=None, headers=None):
        """
        Send a request to the Digital Shadows API.

        :param path: API endpoint path, does not require host. eg. /api/session-user
        :param method:
        :param body:
        :param headers:
        :return: tuple(response, content)
        """
        url = f"{self._url_base}{path}"
        headers = self._headers() if headers is None else headers
        headers["Accept"] = "*/*"
        response, content = super()._request(url, method=method, body=str(body).replace("'", '"'), headers=headers)
        if 200 <= int(response["status"]) <= 299:
            return json.loads(content)
        else:
            body = json.loads(content)
            raise RuntimeError("{} responded with status code {}. {}.".format(url, response["status"], body["message"]))

    def _request_post(self, path, method="POST", body=None, headers=None):
        """
        Send a request to the Digital Shadows API.

        :param path: API endpoint path, does not require host. eg. /api/session-user
        :param method:
        :param body:
        :param headers:
        :return: tuple(response, content)
        """
        url = f"{self._url_base}{path}"
        headers = self._headers() if headers is None else headers

        response, content = super()._request(url, method=method, body=str(body).replace("'", '"'), headers=headers)

        if int(response["status"]) in (200, 204):
            if content != "":
                try:
                    res_text = json.loads(content)
                except json.decoder.JSONDecodeError:
                    return {"status": response["status"], "message": "SUCCESS"}
            else:
                res_text = ""
            post_response = {"status": response["status"], "message": "SUCCESS", "content": []}
            post_response["content"].append(res_text)
            return post_response
        else:
            raise RuntimeError("{} responded with status code {}".format(url, response["status"]))

    def _scrolling_request(self, path, method="GET", body=None, headers=None):
        """
        Scrolls through a paginated response from the Digital Shadows API.

        :param path: API endpoint path, does not require host. eg. /api/session-user
        :param method:
        :param body: View object - requires pagination field, see DSBaseService.paginated decorator
        :return: tuple(response, content)
        """
        assert "pagination" in body
        paginated_view = body
        url = f"{self._url_base}{path}"
        headers = self._headers() if headers is None else headers

        scrolling = True
        while scrolling:
            response, content = super()._request(url, method, body=str(paginated_view).replace("'", '"'), headers=headers)

            if int(response["status"]) == 200:
                data = json.loads(content)
                offset = data["currentPage"]["offset"]
                size = data["currentPage"]["size"]
                total = data["total"]
                if offset + size < total:
                    paginated_view["pagination"]["offset"] = offset + size
                else:
                    scrolling = False
                yield data
            elif int(response["status"]) == 429:
                # rate limited, wait before resuming scroll requests
                time.sleep(1)
            else:
                scrolling = False

    def valid_credentials(self):
        """
        Checks if the provided Digital Shadows credentials are valid.

        :return: bool
        """
        path = "/api/session-user"
        url = f"{self._url_base}{path}"
        response, content = super()._request(url, headers=self._headers(with_content_type=False))
        return int(response["status"]) == 200

    @staticmethod
    def paginated(offset=0, size=500):
        def paginated_decorator(view_function):
            @wraps(view_function)
            def view_wrapper(*args, **kwargs):
                pagination = {"pagination": {"offset": offset, "size": size}}
                view = view_function(*args, **kwargs)
                pagination.update(view)
                return pagination

            return view_wrapper

        return paginated_decorator

    @staticmethod
    def sorted(sort_property, reverse=False):
        def sorted_decorator(view_function):
            @wraps(view_function)
            def view_wrapper(*args, **kwargs):
                sort = {"sort": {"property": sort_property, "direction": "ASCENDING" if reverse else "DESCENDING"}}
                view = view_function(*args, **kwargs)
                sort.update(view)
                return sort

            return view_wrapper

        return sorted_decorator
