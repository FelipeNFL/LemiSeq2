import unittest
import requests
import jwt
from test import test_utils
from core import defines


class FunctionalTestChrompackUpload(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "http://{host}:{port}".format(host=defines.BIOPROCESS_HOST,
                                            port=defines.BIOPROCESS_PORT)

        cls.url_get_list = "{url}/chrompack/all".format(url=url)
        cls.url_upload = "{url}/chrompack".format(url=url)

        cls.db_connection = test_utils.get_database_production()
        cls.collection = 'chrompack'
        cls.user_test = 'test_list_all'

    @classmethod
    def tearDownClass(cls):
        cls.db_connection.remove({'user': cls.user_test}, cls.collection)

    def test_request_without_authorization(self):
        res = requests.get(self.url_get_list, {})
        self.assertEqual(res.status_code, 401)

    def test_wrong_token(self):
        secret_key = 'secret key wrong'
        token = jwt.encode({'user': 'test'}, secret_key).decode()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        res = requests.get(self.url_get_list, {}, headers=headers)

        self.assertEqual(res.status_code, 422)

    def test_get_list(self):

        with open('test/data/test_many_samples.zip', 'rb') as file_test:
            headers = test_utils.get_authorization(self.user_test)
            title_test = 'test_list'
            files = {'file': file_test}

            requests.post(self.url_upload, {'title': title_test}, files=files, headers=headers)

        res = requests.get(self.url_get_list, headers=headers)

        res_json = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res_json), 1)
        self.assertEqual(res_json[0]['title'], title_test)

        for item in res_json:

            keys = list(item.keys())

            self.assertEqual(len(keys), 2)
            self.assertIn('_id', keys)
            self.assertIn('title', keys)

    def test_list_empty(self):
        self.db_connection.remove({'user': self.user_test}, self.collection)

        res = requests.get(self.url_get_list, headers=test_utils.get_authorization(self.user_test))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [])


if "__main__" == __name__:
    unittest.main()