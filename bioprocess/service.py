from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from core import defines
from resources.ResourceChromPack import ResourceChromPack
from resources.ResourceHealth import ResourceHealth

app = Flask(__name__)

CORS(app)

api = Api(app)
api.add_resource(ResourceChromPack, '/chrompack', methods=['POST'])
api.add_resource(ResourceHealth, '/health', methods=['GET'])

app.run(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT, debug=True)