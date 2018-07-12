import unittest
import requests
from commom import defines


class FunctionalTestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.url = 'http://{host}:{port}/{endpoint}'.format(
                                    host=defines.AUTH_HOST,
                                    port=defines.AUTH_PORT,
                                    endpoint='health')

    def test_health_service(self):

        res = requests.get(self.url)
        self.assertEqual(res.text.strip(), "service is running")
        self.assertEqual(res.status_code, 200)

    def test_bad_request(self):

        url = 'http://{host}:{port}'.format(host=defines.AUTH_HOST,
                                            port=defines.AUTH_PORT)

        res = requests.get(url)
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()
