import json
import jwt
from flask_restful import Resource
from flask import request, Response
from commom import defines


class RequestToken(Resource):

    def __init__(self, **kwargs):

        if 'authenticator' not in kwargs:
            raise ValueError('authenticator must be defined')

        authenticator = kwargs['authenticator']
        self._authenticator = authenticator

    def post(self):

        body_request = request.json

        if not body_request:

            return Response('the request body cannot null',
                            status=400,
                            mimetype='application/json')

        if 'username' not in body_request or 'password' not in body_request:

            return Response('the request body is not a valid',
                            status=400,
                            mimetype='application/json')

        username = body_request['username']
        password = body_request['password']

        try:
            validate = self._authenticator.validate(username, password)
        except Exception as e:
            return Response(str(e), status=500)

        if not validate:
            return Response('password or username invalid',
                            status=400,
                            mimetype='application/json')

        try:
            fullname = self._authenticator.get_fullnane(username)
        except Exception as e:
            return Response(str(e), status=500)

        token = jwt.encode({'username': username},
                           {'fullname': fullname},
                           defines._SECRET_KEY_,
                           algorithm='HS256')

        data = json.dumps({'token': token.decode()})

        return Response(data, status=200, mimetype='application/json')
