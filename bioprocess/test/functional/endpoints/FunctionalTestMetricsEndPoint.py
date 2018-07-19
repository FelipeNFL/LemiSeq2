import unittest
import requests
import jwt
from core import defines


class FunctionalTestMetricsEndPoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "http://{host}:{port}/metrics".format(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT)
        cls.user_test = 'test_endpoint_metrics'

    def get_authorization(self):
        secret_key = defines.SECRET_KEY
        token = jwt.encode({'username': self.user_test}, secret_key).decode()
        return {'Authorization': 'Bearer {}'.format(token)}

    def test_request_without_authorization(self):
        res = requests.get(self.url)
        self.assertEqual(res.status_code, 401)

    def test_content_returned(self):
        headers = self.get_authorization()
        res = requests.get(self.url, headers=headers)

        res_expected = {'chrompacks': 0,
                        'samples': 0,
                        'subjects': 0}

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), res_expected)
