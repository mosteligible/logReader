from unittest import TestCase
from unittest.mock import patch

from User import User

from .test_utils import mock_requests


class TestUsers(TestCase):
    @patch("utils.requests.post", side_effect=mock_requests)
    def test_case01():
        pass
