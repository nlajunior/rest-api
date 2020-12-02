from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST


argumentos = reqparse.RequestParser()
argumentos.add_argument('login')
argumentos.add_argument('password')
argumentos.add_argument('organization_key')

class User(Resource):
       
    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404
    
    @jwt_required
    def delete(self, id):
        user = UserModel.find_user(id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying to delete user'}, 500
            return {'message': 'User deleted.'}

        return {'message': 'User not deleted'}, 404

class UserRegister(Resource):
    def post(self):
        data = argumentos.parse_args()

        if UserModel.find_by_login(data['organization_key']):
            return {'message': "The organization already exists."}

        user = UserModel(**data)
        user.save_user()
        return {'message':'User created sucecessfully!'}, 201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = argumentos.parse_args()
        user = UserModel.find_by_login(data['organization_key'])
        if user and safe_str_cmp(user.password, data['password']):
            token = create_access_token(identity=user.id)
            return {'token':token}, 200
        return {'message': 'User unauthorized'}, 401

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti'] # pegando o id do token
        BLACKLIST.add(jwt_id)
        return {'message':'Logged out sucecessfully.'}, 200