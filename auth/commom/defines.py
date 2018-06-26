import os
import sys


def get_environment_variable(tag):

    var = os.environ.get(tag)

    if var is None:
        print(tag + " not defined on ENVIRONMENT")
        print("finishing...")
        sys.exit()

    return var


SECRET_KEY = get_environment_variable('SECRET_KEY')

SERVER_URI = 'ldap://ldap-proxy.epm.br'
SERACH_BASE = 'o=unifesp,c=br'

AUTH_HOST = get_environment_variable('HOST')
AUTH_PORT = get_environment_variable('PORT')
