# app/jwt.py
# JWT configuration and initialization
from flask_jwt_extended import JWTManager
from utils import response_error

jwt = JWTManager()

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return response_error("Missing Authorization Header", 401)
