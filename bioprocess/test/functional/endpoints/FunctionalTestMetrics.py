import unittest
import requests
from core import defines
from test import test_utils


class FunctionalTestMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "http://{host}:{port}/metrics".format(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT)
        cls.user_test = 'test_endpoint_metrics'

    def test_request_without_authorization(self):
        res = requests.get(self.url)
        self.assertEqual(res.status_code, 401)

    def test_content_returned(self):
        headers = test_utils.get_authorization(self.user_test)
        res = requests.get(self.url, headers=headers)

        res_expected = {'chrompacks': 0,
                        'samples': 0,
                        'subjects': 0}

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), res_expected)
