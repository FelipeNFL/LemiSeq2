import os
import logging
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from core import defines
from core.DbConnection import DbConnection
from resources.ResourceChrompack import ResourceChrompack
from resources.ResourceHealth import ResourceHealth


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')


def initialize_directory_data():

    if not os.path.exists(defines.DATA_PATH):
        os.mkdir(defines.DATA_PATH)

    if not os.path.exists(defines.DATA_CHROMPACK):
        os.mkdir(defines.DATA_CHROMPACK)

    if not os.path.exists(defines.DATA_SAMPLE):
        os.mkdir(defines.DATA_SAMPLE)


db_connection = DbConnection(defines.MONGO_HOST,
                             defines.MONGO_USER,
                             defines.MONGO_PASS,
                             defines.MONGO_DB,
                             defines.MONGO_PORT)

params_api = {'upload_folder': 'data',
              'db_connection': db_connection}

app = Flask(__name__)

initialize_directory_data()

CORS(app)

api = Api(app)
api.add_resource(ResourceChrompack, '/chrompack', methods=['POST'], resource_class_kwargs=params_api)
api.add_resource(ResourceHealth, '/health', methods=['GET'])

app.run(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT, debug=True)
