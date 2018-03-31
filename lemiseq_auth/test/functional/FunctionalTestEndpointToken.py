import sys

sys.path.append('commom')

import jwt
import unittest
import requests
import defines
from copy import copy

class FunctionalTestEndpointToken(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.url = 'http://{host}:{port}/{endpoint}'.format(
                                    host=defines._AUTH_HOST_,
                                    port=defines._AUTH_PORT_,
                                    endpoint='token')

        self.data = {'username': 'teste', 'password': 'teste'}

    def test_get_token(self):

        res = requests.get(self.url, json=self.data)
        data = jwt.decode(res.json()['token'],
                          defines._SECRET_KEY_,
                          algorithms=['HS256'])

        self.assertEqual(data, {'username': self.data['username']})
        self.assertEqual(res.status_code, 200)

    def test_login_invalid(self):

        res = requests.get(self.url, json={'username': 'teste',
                                           'password': 'teste'})

        self.assertEqual(res.text, 'password or username invalid')
        self.assertEqual(res.status_code, 400)

    def test_invalid_json(self):

        res = requests.get(self.url, json={})

        self.assertEqual(res.text, 'the request body is not a valid')
        self.assertEqual(res.status_code, 400)

    def test_empty_json(self):

        res = requests.get(self.url)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'the request body cannot null')

if __name__ == '__main__':
    unittest.main()
