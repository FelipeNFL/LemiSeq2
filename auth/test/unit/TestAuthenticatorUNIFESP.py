import unittest
from commom import defines
from authenticators.AuthenticatorUNIFESP import AuthenticatorUNIFESP


class TestAuthenticatorUNIFESP(unittest.TestCase):

    def test_init(self):

        with self.assertRaises(TypeError):
            AuthenticatorUNIFESP(uri=123, base='123')

        with self.assertRaises(TypeError):
            AuthenticatorUNIFESP(uri='123', base=123)

        AuthenticatorUNIFESP('123','123')

    def test_validate(self):

        authenticator = AuthenticatorUNIFESP(defines.SERVER_URI,
                                             defines.SERACH_BASE)

        with self.assertRaises(TypeError):
            authenticator.validate(123, '123')

        with self.assertRaises(TypeError):
            authenticator.validate('123', 123)

        authenticator.validate('123', '123')


if __name__=='__main__':
    unittest.main()
