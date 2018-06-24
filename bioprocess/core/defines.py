import os
import sys
import logging


def get_environment_variable(variable_name):

    variable = os.environ.get(variable_name)

    if not variable:
        logging.error('{} environment variable is not defined'.format(variable_name))
        logging.info('The service will be shutdown')
        sys.exit()

    return variable


MONGO_HOST = get_environment_variable('MONGO_HOST')
MONGO_PORT = int(get_environment_variable('MONGO_PORT'))
MONGO_USER = get_environment_variable('MONGO_USERNAME')
MONGO_PASS = get_environment_variable('MONGO_PASSWORD')
MONGO_DB = get_environment_variable('MONGO_DATABASE')

BIOPROCESS_HOST = get_environment_variable('BIOPROCESS_HOST')
BIOPROCESS_PORT = get_environment_variable('BIOPROCESS_PORT')

SECRET_KEY = get_environment_variable('SECRET_KEY')

DATA_PATH = 'data'

DATA_CHROMPACK = DATA_PATH + '/chrompack'
DATA_SAMPLE = DATA_PATH + '/samplepool'