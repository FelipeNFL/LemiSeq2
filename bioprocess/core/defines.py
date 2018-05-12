import os
import sys
import logging


def get_environment_variable(variable_name):

    variable = os.environ.get(variable_name)

    if not variable:
        logging.error('{} environment variable is not defined')
        logging.info('The service will be shutdown')
        sys.exit()

    return variable


MYSQL_HOST = get_environment_variable('MYSQL_HOST')
MYSQL_PORT = get_environment_variable('MYSQL_PORT')
MYSQL_USER = get_environment_variable('MYSQL_USERNAME')
MYSQL_PASS = get_environment_variable('MYSQL_PASSWORD')
MYSQL_DB = get_environment_variable('MYSQL_DATABASE')
BIOPROCESS_HOST = get_environment_variable('BIOPROCESS_HOST')
BIOPROCESS_PORT = get_environment_variable('BIOPROCESS_PORT')
