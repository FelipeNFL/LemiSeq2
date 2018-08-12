import os
import logging
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_simple import JWTManager
from core import defines
from core.DbConnection import DbConnection
from resources.ResourceChrompack import ResourceChrompack
from resources.ResourceHealth import ResourceHealth
from resources.ResourceMetrics import ResourceMetrics
from resources.ResourceChrompackList import ResourceChrompackList
from resources.ResourceChrompackUpload import ResourceChrompackUpload


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
app.config["JSON_SORT_KEYS"] = False
app.config['JWT_SECRET_KEY'] = defines.SECRET_KEY

JWTManager(app)

api.add_resource(ResourceChrompackUpload, '/chrompack', methods=['POST'], resource_class_kwargs=params_api)
api.add_resource(ResourceChrompack, '/chrompack/<string:id>', methods=['DELETE'], resource_class_kwargs=params_api)
api.add_resource(ResourceChrompackList, '/chrompack/all', methods=['GET'], resource_class_kwargs=params_api)
api.add_resource(ResourceHealth, '/health', methods=['GET'])
api.add_resource(ResourceMetrics, '/metrics', methods=['GET'], resource_class_kwargs=params_api)

app.run(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT, debug=True)
