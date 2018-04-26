import sys

sys.path.append('authenticators')

import hashlib
import logging
from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPSocketOpenError
from Authenticator import Authenticator

class AuthenticatorUNIFESP(Authenticator):

    def __init__(self, uri, base):

        if not isinstance(uri, str):
            raise TypeError('uri must be a string, not a {type}'.format(
                                                        type=type(uri)))

        if not isinstance(base, str):
            raise TypeError('base must be a string, not a {type}'.format(
                                                        type=type(base)))

        self._uri = uri
        self._base = base

    def _get_entries(self, username):

        server = Server(self._uri)
        search_filter = '(uid={username})'.format(username=username)

        try:
            with Connection(server, auto_bind=True) as conn:
                conn.search(self._base, search_filter, attributes=['*'])
                return conn.entries
        except LDAPSocketOpenError as e:
            raise ConnectionError(str(e) + ' | Verify the credentials')

    def _get_password(self, entries):

        try:

            first_entry = entries[0]
            password_list = first_entry['userPassword']
            md5_password = password_list[1].decode()[5:]

            return md5_password

        except Exception as e:

            logging.error(e)
            return None

    def validate(self, username, password):

        if not isinstance(username, str):
            raise TypeError('username must be a string, not {type}'.format(
                                                      type=type(username)))

        if not isinstance(password, str):
            raise TypeError('password must be a string, not {type}'.format(
                                                      type=type(password)))

        entries = self._get_entries(username)

        if not entries:
            return False

        password_saved = self._get_password(entries)
        password_passed_in_md5 = hashlib.md5(password.encode()).hexdigest()

        return password_saved == password_passed_in_md5
