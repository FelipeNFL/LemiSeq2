import jwt
import unittest
import requests
import getpass
from commom import defines


class FunctionalTestEndpointToken(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.url = 'http://{host}:{port}/{endpoint}'.format(
                                    host=defines.AUTH_HOST,
                                    port=defines.AUTH_PORT,
                                    endpoint='token')

        cls.data = {'username': input('Digite seu usuário UNIFESP: '),
                    'password': getpass.getpass(prompt='Digite sua senha UNIFESP: ')}

    def test_get_token(self):

        res = requests.post(self.url, json=self.data)
        data = jwt.decode(res.json()['token'],
                          defines.SECRET_KEY,
                          algorithms=['HS256'])

        self.assertEqual(data['username'], self.data['username'])
        self.assertNotEqual(data['fullname'], None)
        self.assertEqual(res.status_code, 200)

    def test_login_invalid(self):

        res = requests.post(self.url, json={'username': 'teste',
                                            'password': 'teste'})

        self.assertEqual(res.text, 'password or username invalid')
        self.assertEqual(res.status_code, 400)

    def test_invalid_json(self):

        res = requests.post(self.url, json={'teste': 'teste'})

        self.assertEqual(res.text, 'the request body is not a valid')
        self.assertEqual(res.status_code, 400)

    def test_empty_json(self):

        res = requests.post(self.url)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'the request body cannot null')


if __name__ == '__main__':
    unittest.main()
