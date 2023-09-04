from typing import Dict
from unittest import TestCase
from unittest.mock import patch

from utils import collectResponse, retreiveAllClients


class RequestMethod:
    def __init__(self, method: str = "POST") -> None:
        self.method = method


class MockRequest:
    def __init__(self, url: str, method: str) -> None:
        self.url = url
        self.request = RequestMethod()
        self.status_code = 200

    def raise_for_status(self):
        return True

    def json(self):
        if self.url == "https://www.clientendpoint.io":
            return {
                "status": "200",
                "id": "clientid",
                "name": "testClientName",
                "plan": "small",
                "token": "lisudnclsiuncalsiud",
            }
        elif self.url == "https://www.allclients.io":
            return {}


def mock_requests(url: str) -> MockRequest:
    if url == "https://www.clientendpoint.io":
        return MockRequest(url=url, method="POST")
    elif url == "https://www.allclients.io":
        return MockRequest(url=url, method="GET")


class TestUtils(TestCase):
    @patch("utils.requests.post", side_effect=mock_requests)
    def testCollectResponse(self, mock_post):
        urls = {
            "https://www.clientendpoint.io": {
                "id": "clientid",
                "token": "appinstanceauthtoken",
            }
        }
        expResponse = {
            "status": "200",
            "id": "clientid",
            "name": "testClientName",
            "plan": "small",
            "token": "lisudnclsiuncalsiud",
        }
        for url, payload in urls.items():
            clientResponse = collectResponse(url, payload)
            self.assertDictEqual(clientResponse, expResponse)

    @patch("utils.requests.get", side_effect=mock_requests)
    def testRetreiveAllClients(self, mock_get):
        urls = {
            "https://www.allclients.io": {
                "application_instance": "appname",
                "token": "avalidtokenvalue",
            }
        }
