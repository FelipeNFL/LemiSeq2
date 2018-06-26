import unittest
import getpass
from commom import defines
from authenticators.AuthenticatorUNIFESP import AuthenticatorUNIFESP


class FunctionalTestAuthenticator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.login_correct = {'username': input('Digite seu usuário UNIFESP: '),
                             'password': getpass.getpass(prompt='Digite sua senha UNIFESP: ')}

        cls.authenticator = AuthenticatorUNIFESP(defines.SERVER_URI,
                                                 defines.SERACH_BASE)

    def test_access_data_invalid(self):

        authenticator = AuthenticatorUNIFESP('123', '123')

        with self.assertRaises(ConnectionError):
            authenticator.validate('123', '123')

    def test_validate_true(self):

        validate = self.authenticator.validate(self.login_correct['username'],
                                               self.login_correct['password'])
        self.assertTrue(validate)

    def test_get_fullname(self):

        fullname = self.authenticator.get_fullname(self.login_correct['username'])

        self.assertIsNotNone(fullname)

    def test_username_wrong(self):

        validate = self.authenticator.validate('wrong',
                                               self.login_correct['password'])
        self.assertFalse(validate)

    def test_password_wrong(self):

        validate = self.authenticator.validate('teste', 'teste')
        self.assertFalse(validate)


if __name__ == '__main__':
    unittest.main()
