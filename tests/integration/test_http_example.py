import unittest

import requests

from py_project import __version__


class TestAzfnHttpTrigger(unittest.TestCase):
    def setUp(self):
        pass

    def test_call_http_trigger_should_return_version(self):
        # given
        url = "localhost:8080/api/trigger/example"
        expected_content = __version__
        expected_status_code = 200

        # when
        response = requests.get(f"http://{url}")
        returned_content = response.content.decode("UTF-8")

        # Then
        assert response.status_code == expected_status_code
        assert returned_content == expected_content
