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
DATA_WORK_DIR = DATA_PATH + '/work'
CONFIG_PATH = 'config.json'

PHRED_BIN = 'tools/phred'
PHRED_PARAMETERS_FILE = 'tools/data/phred_parameters.dat'
PHD2FAS_BIN = 'tools/phd2fas'
PHRAP_BIN = 'tools/phrap'
