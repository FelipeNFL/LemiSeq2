import jwt
from flask_restful import Resource
from flask import request, Response
from commom import defines
from authenticators import Authenticator

class RequestToken(Resource):

    def __init__(self, **kwargs):

        if 'authenticator' not in kwargs:
            raise ValueError('authenticator must be defined')

        authenticator_obj = kwargs['authenticator']

        if not issubclass(type(authenticator_obj), Authenticator):
            raise TypeError('authenticator must be a Authenticator instance, '\
                            'not {type}'.format(type(authenticator_obj)))

        self._authenticator = authenticator_obj

    def get(self):

        body_request = request.json

        if 'username' or 'password' not in request.json:

            return Response('the request body is not a valid',
                             status=400,
                             mimetype='application/json')

        username = request.json['username']
        password = request.json['password']

        if not self._authenticator.validate(username, password):

            return Response('password or username invalid',
                            status=400,
                            mimetype='application/json')

        token = jwt.encode({'username': username},
                            defines._SECRET_KEY_,
                            algorithm='HS256')

        return Response({'token': token},
                        status=200,
                        mimetype='application/json')
