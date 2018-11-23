import os
import logging
import json
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
from resources.ResourceSubject import ResourceSubject
from resources.ResourceManagerSubject import ResourceManagerSubject
from resources.ResourceBuildSubject import ResourceBuildSubject
from resources.ResourceSubjectMatrixAll import ResourceSubjectMatrixAll
from resources.ResourceSubjectMatrixEmpty import ResourceSubjectMatrixEmpty
from resources.ResourceManagerSlot import ResourceManagerSlot
from resources.ResourceUpdateSlot import ResourceUpdateSlot

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')


def initialize_directory_data():

    if not os.path.exists(defines.DATA_PATH):
        os.mkdir(defines.DATA_PATH)

    if not os.path.exists(defines.DATA_WORK_DIR):
        os.mkdir(defines.DATA_WORK_DIR)


db_connection = DbConnection(defines.MONGO_HOST,
                             defines.MONGO_USER,
                             defines.MONGO_PASS,
                             defines.MONGO_DB,
                             defines.MONGO_PORT)

with open('config.json', 'r') as fp:
    configs = json.loads(fp.read())

params_api = {'upload_dir': defines.DATA_WORK_DIR,
              'db_connection': db_connection,
              'configs': configs}

app = Flask(__name__)

initialize_directory_data()

CORS(app)

api = Api(app)
app.config["JSON_SORT_KEYS"] = False
app.config['JWT_SECRET_KEY'] = defines.SECRET_KEY

JWTManager(app)

api.add_resource(ResourceChrompackUpload, '/chrompack',
                 methods=['POST'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceChrompack,
                 '/chrompack/<string:id>',
                 methods=['DELETE'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceChrompackList,
                 '/chrompack/all',
                 methods=['GET'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceSubject,
                 '/chrompack/<string:id_chrompack>/subject',
                 methods=['GET'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceManagerSubject,
                 '/chrompack/<string:id_chrompack>/subject/<string:name>',
                 methods=['POST'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceBuildSubject,
                 '/chrompack/<string:id_chrompack>/subject/<string:name>/build',
                 methods=['POST'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceSubjectMatrixAll,
                 '/chrompack/<string:id_chrompack>/subject/matrix',
                 methods=['GET'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceSubjectMatrixEmpty,
                 '/subject/matrix/default',
                 methods=['GET'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceUpdateSlot,
                 '/chrompack/<string:id_chrompack>/slot/<string:slot>/subject/<string:subject>',
                 methods=['PUT'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceManagerSlot,
                 '/chrompack/<string:id_chrompack>/slot/<string:slot>/subject',
                 methods=['DELETE', 'GET'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceMetrics,
                 '/metrics',
                 methods=['GET'],
                 resource_class_kwargs=params_api)

api.add_resource(ResourceHealth,
                 '/health',
                 methods=['GET'])

app.run(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT, debug=True)
