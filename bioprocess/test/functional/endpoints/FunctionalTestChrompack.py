import unittest
import requests
import jwt
from test import test_utils
from core import defines


class FunctionalTestChrompack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.url = "http://{host}:{port}/chrompack".format(host=defines.BIOPROCESS_HOST,
                                                          port=defines.BIOPROCESS_PORT)

        cls.db_connection = test_utils.get_database_production()

        cls.collection = 'chrompack'
        cls.user_test = 'test_list_all'

    @classmethod
    def tearDownClass(cls):
        cls.db_connection.remove({'user': cls.user_test}, cls.collection)

    def test_request_without_authorization(self):
        url = '{url}/{id}'.format(url=self.url, id='5b7091ba8dff0c000ec3eca4')
        res = requests.delete(url)
        self.assertEqual(res.status_code, 401)

    def test_wrong_token(self):
        secret_key = 'secret key wrong'
        token = jwt.encode({'user': 'test'}, secret_key).decode()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        url = '{url}/{id}'.format(url=self.url, id='5b7091ba8dff0c000ec3eca4')
        res = requests.delete(url=url, json={}, headers=headers)

        self.assertEqual(res.status_code, 422)

    def test_delete_id_not_existing(self):

        url = '{url}/{id}'.format(url=self.url, id='5b7091ba8dff0c000ec3eca4')
        res = requests.delete(url=url, headers=test_utils.get_authorization(self.user_test))

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'No record deleted')

    def test_delete_successful(self):

        headers = test_utils.get_authorization(self.user_test)

        with open('test/data/test_many_samples.zip', 'rb') as fp:

            files = {'file': fp}
            title_test = 'test_delete_successful'
            res = requests.post(self.url, {'title': title_test}, files=files, headers=headers)

        self.assertEqual(res.status_code, 200)

        url_get_list = '{url}/{endpoint}'.format(url=self.url, endpoint='all')
        res = requests.get(url_get_list, headers=headers)

        id_chrompack = res.json()[0]['_id']

        url_delete = '{url}/{id}'.format(url=self.url, id=id_chrompack)
        res = requests.delete(url_delete, headers=headers)

        self.assertEqual(res.status_code, 200)

        res = requests.get(url_get_list, headers=headers)

        self.assertEqual(res.json(), [])


if "__main__" == __name__:
    unittest.main()