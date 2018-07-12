from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from commom import defines
from resources.RequestToken import RequestToken
from resources.ServiceHealth import ServiceHealth
from authenticators.AuthenticatorUNIFESP import AuthenticatorUNIFESP

authenticator = AuthenticatorUNIFESP(defines.SERVER_URI, defines.SERACH_BASE)
params_api = {"authenticator": authenticator}

app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(ServiceHealth, '/health', methods=['GET'])
api.add_resource(RequestToken, '/token', resource_class_kwargs=params_api, methods=['POST'])

app.run(host=defines.AUTH_HOST, port=defines.AUTH_PORT, debug=True)
