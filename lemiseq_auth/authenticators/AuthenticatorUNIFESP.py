import hashlib
from ldap3 import Server, Connection
from .Authenticator import Authenticator

class AuthenticatorUNIFESP(Authenticator):

    def __init__(self, uri, base):

        if not isinstance(uri, str):
            raise TypeError('uri must be a string, not a {type}'.format(
                                                             type(uri)))

        if not isinstance(base, str):
            raise TypeError('base must be a string, not a {type}'.format(
                                                             type(base)))

        self._uri = uri
        self._base = base

    def _get_entries(self, username):

        server = Server(self._uri)
        search_filter = '(uid={username})'.format(username=username)

        with Connection(server, auto_bind=True) as conn:
            conn.search(self._base, search_filter, attributes=['*'])
            return conn.entries

    def _get_password(self, entries):

        first_entry = entries[0]
        password_list = first_entry['userPassword']
        md5_password = password_list[1].decode()[5:]

        return md5_password

    def validade(self, username, password):

        if not isinstance(username, str):
            raise TypeError('username must be a string, not {type}'.format(
                                                           type(username)))

        if not isinstance(password, str):
            raise TypeError('password must be a string, not {type}'.format(
                                                           type(password)))

        entries = self._get_entries(username)

        if not entries:
            return False

        password_saved = self._get_password(entries)
        password_passed_in_md5 = hashlib.md5('felipe0206'.encode()).hexdigest()

        return password_saved == password_passed_in_md5
