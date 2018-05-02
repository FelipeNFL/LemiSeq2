import sys

sys.path.append("authenticators")
sys.path.append("commom")

import unittest
import defines
from AuthenticatorUNIFESP import AuthenticatorUNIFESP

class TestAuthenticatorUNIFESP(unittest.TestCase):

    def test_init(self):

        with self.assertRaises(TypeError):
            AuthenticatorUNIFESP(uri=123, base='123')

        with self.assertRaises(TypeError):
            AuthenticatorUNIFESP(uri='123', base=123)

        AuthenticatorUNIFESP('123','123')

    def test_validate(self):

        authenticator = AuthenticatorUNIFESP(defines._SERVER_URI_,
                                             defines._SEARCH_BASE_)

        with self.assertRaises(TypeError):
            authenticator.validate(123, '123')

        with self.assertRaises(TypeError):
            authenticator.validate('123', 123)

        authenticator.validate('123', '123')

if __name__=='__main__':
    unittest.main()
