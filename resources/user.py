from flask_restful import Resource, reqparse
from models.user import UserModel

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


