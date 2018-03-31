from flask import Flask
from flask_restful import Api
from commom import defines
from resources.RequestToken import RequestToken
from resources.ServiceHealth import ServiceHealth
from authenticators.AuthenticatorUNIFESP import AuthenticatorUNIFESP

authenticator = AuthenticatorUNIFESP(defines._SERVER_URI_, defines._SEARCH_BASE_)
params_api = {"authenticator": authenticator}

app = Flask(__name__)

api = Api(app)

api.add_resource(ServiceHealth, '/health', methods=['GET'])
api.add_resource(RequestToken,
                 '/token',
                 resource_class_kwargs=params_api,
                 methods=['GET'])

app.run(host=defines._AUTH_HOST_, port=defines._AUTH_PORT_, debug=True)
