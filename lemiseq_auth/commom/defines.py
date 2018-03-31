import os
import sys


def get_environ(tag):
    var = os.environ.get(tag)
    if not var:
        print(tag + " not defined on ENVIRON")
        print("finishing...")
        sys.exit()

        return var


_SECRET_KEY_ = 'essa key precisa ser trocada'

_SERVER_URI_ = 'ldap://ldap-proxy.epm.br'
_SEARCH_BASE_ = 'o=unifesp,c=br'

_AUTH_HOST_ = get_environ('HOST')
_AUTH_PORT_ = get_environ('PORT')
